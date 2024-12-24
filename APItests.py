import requests 
import json
from PIL import Image, ImageTk
from io import BytesIO
import tkinter as tk

window = tk.Tk()

booktitle = "Amish Tripathi"

response = requests.get(f"https://www.googleapis.com/books/v1/volumes?q={booktitle}&maxResults=5")

data = response.json()

whatiwant = data["items"][0]["volumeInfo"]["imageLinks"]["thumbnail"]

# "Pretty printing" the json
# print(json.dumps(whatiwant, indent=4))

imageresponse = requests.get(whatiwant)

img = Image.open(BytesIO(imageresponse.content))



tk_img = ImageTk.PhotoImage(img)

window.tk_img = tk_img

imagelabel = tk.Label(window, image = tk_img )
imagelabel.pack()

window.mainloop()
