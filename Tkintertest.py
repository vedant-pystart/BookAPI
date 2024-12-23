import tkinter as tk
import requests

booklist = []


def getbooklist():

    # Resets all labels
    for label in booklist:
        label.destroy()
    booktitle = entry.get() 

    # Uses Google books API
    response = requests.get(f"https://www.googleapis.com/books/v1/volumes?q={booktitle}")
    data = response.json()

    i = 1
    # Creates loop which makes numbered list of books.
    # Creates loop which makes numbered list of books.
    for book in data['items']:
        title = book['volumeInfo'].get('title', 'No title available')
        author = book['volumeInfo'].get('authors', ['No author available'])[0]  # Getting the first author, if available
        page_count = book['volumeInfo'].get('pageCount', 'Page count not available')

        listitem = (f"{i}. {title}")
        i = i + 1

        # Create a button for each book
        addlistitem = tk.Button(window, text=listitem, command=lambda t=title, a=author, p=page_count: clickbook(t, a, p))
        addlistitem.pack()

        # Append the button to booklist to manage future clearing
        booklist.append(addlistitem)


def clickbook(title, author, pagecount, ):
    window2 = tk.Tk()
    window2.title(title)
    titlelabel = tk.Label(window2, text = f"Title: {title}")
    authorlabel = tk.Label(window2, text = f"Author: {author}")
    pagecountlabel = tk.Label(window2, text = f"Page Count: {pagecount}")

    titlelabel.pack()
    authorlabel.pack()
    pagecountlabel.pack()

    window2.mainloop()
    

# Main Window
window = tk.Tk()
window.title("Vedant's Book Search")

# Creates a label called label which is text asking which book/author
label = tk.Label(window, text = "Enter the book or author you wish to find: ")
label.pack()

# Creates a box in which you enter information
entry = tk.Entry(window)
entry.pack()

# Creates a search button
button  = tk.Button(window, text = "Search", command = getbooklist)
button.pack()

# Keeps the window persistant
window.mainloop()