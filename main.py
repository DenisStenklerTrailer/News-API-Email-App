import requests
import Send_Email

api_key = "ec9307c61e1e45919380149b1b44af87"

# https://www.24ur.com/
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-01-06&sortBy=publishedAt&apiKey=ec9307c61e1e45919380149b1b44af87"

# Make a request
request = requests.get(url)
# Get dictionary with data
content = request.json()

MessageToSend = ""

for article in content["articles"]:
    if article["title"] != None:
        MessageToSend = MessageToSend + article["title"] + "\n" + article["description"] + 2*"\n"

with open("test.txt", "w") as file:
    file.write(MessageToSend)

MessageToSend = MessageToSend.encode("utf-8")


# Send_Email.send_email(MessageToSend)

