# Choosing a random number between 1 and 100.
from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
    """Checks answer against guess. Returns the number of turns remaining"""
    if guess > answer:
        print("Too high! Guess again.")
        return turns - 1
    elif guess < answer:
        print("Too low! Guess again.")
        return turns - 1
    else:
        print(f"You got it, the answer is {answer}")

# Make a function to set difficulty level.
def set_difficulty():
    level = input("Choose a difficulty, type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    print("Welcome to the guessing game! \nI am thinking of a number between 1 and 100" )
    answer = randint(1, 100)
    print(f"pssst! the answer is {answer}")
    turns = set_difficulty()

    # Repeat the guessing functionality if they guess it wrong.
    guess = 0
    while guess != answer:
        # Let the user guess a number.
        guess = int(input("Guess a number: "))
        turns = check_answer(guess, answer, turns)
        print(f"You have {turns} more guesses left.")
        if turns == 0:
            print("You have run out of guesses. You have lost.")
            return

game()

# Track the number of turns and reduce by 1 if they get it wrong.



#