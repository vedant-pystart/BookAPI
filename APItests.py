import requests 
import json
from PIL import Image
from io import BytesIO

booktitle = "Amish Tripathi"

response = requests.get(f"https://www.googleapis.com/books/v1/volumes?q={booktitle}&maxResults=5")

data = response.json()

whatiwant = data["items"][0]["volumeInfo"]["imageLinks"]["thumbnail"]

# "Pretty printing" the json
# print(json.dumps(whatiwant, indent=4))

print(whatiwant)

imageresponse = requests.get(whatiwant)

img = Image.open(BytesIO(imageresponse.content))

img.show()