# STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

# TODO 2. - Get the day before yesterday's closing stock price

# TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

# TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

# TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").


import requests
from datetime import date, timedelta
from twilio.rest import Client

account_sid = ID
auth_token = TOKEN

stock_api = API

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"

STOCK_PARAM = {"apikey": stock_api,
               "function": "TIME_SERIES_DAILY",
               "symbol": STOCK_NAME}

should_text = False

today = date.today()
yesterday = date.today() - timedelta(days=1)
d_b_yesterday = date.today() - timedelta(days=2)

response = requests.get(url=STOCK_ENDPOINT, params=STOCK_PARAM)
response.raise_for_status()
yt_stock_data = response.json()["Time Series (Daily)"][f"{yesterday}"]
yt2_stock_data = response.json()["Time Series (Daily)"][f"{d_b_yesterday}"]

yt_closing = float(yt_stock_data["4. close"])
yt2_closing = float(yt2_stock_data["4. close"])

# print(yt_stock_data, yt2_stock_data)
# print(type(yt_closing), yt2_closing)

diff = yt_closing - yt2_closing
up_down = None
if diff > 0:
    up_down = "🔼"
else:
    up_down = "🔽"


percentage = round((diff / yt_closing) * 100)

if abs(percentage) > 5.0:
    should_text = True


# TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

## STEP 2: https://newsapi.org/
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

# TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


## STEP 3: Use twilio.com/docs/sms/quickstart/python
# to send a separate message with each article's title and description to your phone number.

# TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

# TODO 9. - Send each article as a separate message via Twilio.
def text_news():
    NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
    news_api = "6ebf236ee4554c1ab596576c24b31370"
    news_param = {"q": COMPANY_NAME,
                  "apiKey": news_api,
                  }

    response = requests.get(url=NEWS_ENDPOINT, params=news_param)
    response.raise_for_status()

    news_data = response.json()
    news_3 = news_data["articles"][:3]
    news_text = [f"{STOCK_NAME}{up_down}{diff}%\nHeadline: {article['title']}.\nBrief: {article['description']}" for article in news_3]

    client = Client(account_sid, auth_token)

    for article in news_text:
        message = client.messages.create(
            from_=FROM
            to= TO
            body=article
        )


if should_text:
    text_news()

# Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
