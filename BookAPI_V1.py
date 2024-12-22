import requests
import tkinter as tk

cont = "Y"
while cont == "Y":
    booktitle = input("Enter the book or author you wish to find: ")

    response = requests.get(f"https://www.googleapis.com/books/v1/volumes?q={booktitle}&maxResults=40")
    data = response.json()

    i = 1

    for book in data['items']:
        title = book['volumeInfo'].get('title', 'No title available')
        print(f"{i}. {title}")
        i = i + 1

    index = input("Tell me what you want: ")
    index = int(index) - 1

    pagecount = data['items'][index]['volumeInfo'].get('pageCount', 'Page count not available')
    finaltitle = data['items'][index]['volumeInfo'].get('title')

    print(f"{finaltitle} has {pagecount} pages")

    cont = input("Would you like to search again? (Y/N): ")
    print()
    if cont == "N":
        break




    