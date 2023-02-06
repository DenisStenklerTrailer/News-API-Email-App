import requests
import Send_Email

api_key = "ec9307c61e1e45919380149b1b44af87"
topic = "tesla"


# https://www.24ur.com/
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "from=2023-01-06&" \
      "apiKey=ec9307c61e1e45919380149b1b44af87&" \
      "language=en"

# Make a request
request = requests.get(url)
# Get dictionary with data
content = request.json()

MessageToSend = "Subject: Today's news:" + "\n"

for article in content["articles"][:20]:
    if article["title"] != None:
        MessageToSend = MessageToSend + article["title"] +\
                        "\n" + article["description"] +\
                        "\n" + article["url"] + 2*"\n"


#with open("test.txt", "w") as file:
#    file.write(MessageToSend)
print(MessageToSend)
MessageToSend = MessageToSend.encode("utf-8")

Send_Email.send_email(MessageToSend)

