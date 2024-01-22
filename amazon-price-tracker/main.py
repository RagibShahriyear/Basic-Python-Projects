import requests
import lxml
import smtplib
from bs4 import BeautifulSoup


sender = SENDER
receiver = RECEIVER
password = PASSWORD
amazon_url = "https://www.amazon.com/Acer-EZ321Q-31-5-Monitor-White/dp/B07YGY3RLN/ref=sr_1_6?qid=1691238489&refinements=p_n_feature_twenty_browse-bin%3A72511692011%2Cp_n_feature_twenty-one_browse-bin%3A73824531011&rnid=73824515011&s=pc&sr=1-6&th=1"

r = requests.get(
    url=amazon_url,
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.36",
        "Accept-Language": "en-US,en;q=0.9,bn;q=0.8",
    },
)

soup = BeautifulSoup(r.text, "lxml")


price = float(soup.find(class_="a-price-whole").get_text())
message = "Subject:Price dropped on your favorite item from Amazon.\n\nGet that monitor my boi."

if price < 1000.0:
    try:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=sender, password=password)
            connection.sendmail(from_addr=sender, to_addrs=receiver, msg=message)
    except SMTPException:
        print("Error: unable to send email")
