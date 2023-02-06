import requests

url = "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Bird_Diversity_2013.png/300px-Bird_Diversity_2013.png"

request = requests.get(url)

image = request.content

with open("image.jpg", "wb") as file:
    file.write(image)
