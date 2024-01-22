import spotipy
from spotipy.oauth2 import SpotifyOAuth
import speech_recognition as sr

scope = "user-read-currently-playing playlist-read-private playlist-modify-private"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope=scope,
        redirect_uri="http://google.com/",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
    )
)

user_id = sp.current_user()["id"]
song_uri = []


def add_song():
    current_playing_artist = sp.currently_playing()["item"]["album"]["artists"][0][
        "name"
    ]
    current_playing_song = sp.currently_playing()["item"]["name"]
    current_playing_URI = sp.currently_playing()["item"]["uri"]
    song_uri.append(current_playing_URI)
    playlist_id = sp.current_user_playlists()["items"][0]["id"]
    # playlist_name = sp.current_user_playlists()['items'][0]['name']
    print(
        f"Spotify is currently playing : {current_playing_song} by {current_playing_artist}"
    )
    sp.playlist_add_items(playlist_id, song_uri)


def voice_command():
    listener = sr.Recognizer()

    with sr.Microphone() as source:
        print("listening..")
        listener.pause_threshold = 0.5
        voice = listener.listen(source)
        try:
            print("Waiting for your command: ")
            command = listener.recognize_google(voice, language="en-us")
            if "add" or "playlist" in command:
                add_song()
                print(f"The command is: {command}")

        except Exception as e:
            print(e)
            print("Say that again")
            return "None"


if __name__ == "__main__":
    voice_command()
