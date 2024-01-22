import smtplib
import datetime as dt
import random

my_email = EMAIL
your_email = EMAIL2
password = PASSWORD


now = dt.datetime.now()
if now.weekday() == 2:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        # reading all the lines from a text file
        quote_of_the_day = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=your_email,
            msg=f"Subject:Greetings!\n\n{quote_of_the_day}",
        )
