
# # Scrape and Display the Data

# import requests
# from bs4 import BeautifulSoup
# import itertools
# from staticStuff import book, display, fillObjArray
# import database

# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', "Upgrade-Insecure-Requests": "1",
#            "DNT": "1", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate"}


# def getURL() :

#     baseurl = 'https://libgen.is/search.php?req=&open=0&res=25&view=detailed&phrase=0&column=def'

#     searchKey = str(input('Enter search Keyword : '))
#     searchKey = searchKey.split(' ')

#     query = ''

#     for i in range(0, len(searchKey)):
#         query += searchKey[i] + '+'

#     query = query[: -1]
#     baseurl = baseurl.split('?req=')
#     baseurl[0] += '?req='
#     baseurl[0] += query
#     return (baseurl[0] + baseurl[1])



# def downloadPrompt(objarray) :

#     downnum = int(
#         input('Enter Book No. to download book otherwise enter -1 to Exit -\n'))

#     if(downnum == -1):
#         return

#     if(objarray[downnum]["Extension"] != "pdf") :
#         print('Not a pdf!')
#         return

#     conn = database.connect()
#     database.createTable(conn)

#     database.addBook(conn, objarray[downnum]["Title"], objarray[downnum]["Author"], objarray[downnum]["pages"])
    
#     downlink = objarray[downnum]["downloadlink"]
    
#     downpage = requests.get(downlink)
    
#     dsoup = BeautifulSoup(downpage.content, 'html.parser')
    
#     dlink = dsoup.find('a', string="GET")["href"]

#     fl = requests.get(dlink, headers = headers)

#     with open(str(objarray[downnum]['Title']) + '.pdf', 'wb') as f:
#         f.write(fl.content)

#     print(str(objarray[downnum]['Title']) +
#           " is added to your Library!\n")



# def findBook():

#     url = getURL()
#     res = requests.get(url, verify=False)
#     soup = BeautifulSoup(res.content, 'html.parser')

#     size = 0
#     objarray = []

#     fillObjArray(soup, objarray, size)

#     display(objarray, size)
    
#     downloadPrompt(objarray)



import tkinter as tk
from tkinter import simpledialog, messagebox
from bs4 import BeautifulSoup
import requests
import database
from staticStuff import fillObjArray, display

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    "Upgrade-Insecure-Requests": "1",
    "DNT": "1",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate"
}

def getURL(searchKey):
    baseurl = 'https://libgen.is/search.php?req=' + searchKey + '&open=0&res=25&view=detailed&phrase=0&column=def'
    return baseurl

def downloadBook(conn, book):
    if book["Extension"] != "pdf":
        messagebox.showerror("Error", "Not a PDF!")
        return

    downlink = book["downloadlink"]
    downpage = requests.get(downlink, verify=False)
    dsoup = BeautifulSoup(downpage.content, 'html.parser')
    dlink = dsoup.find('a', string="GET")["href"]

    fl = requests.get(dlink, headers=headers, verify=False)

    with open(f"{book['Title']}.pdf", 'wb') as f:
        f.write(fl.content)

    database.addBook(conn, book["Title"], book["Author"], book["pages"])
    messagebox.showinfo("Success", f"{book['Title']} is added to your Library!")

def findBook(searchKey, listbox):
    conn = database.connect()
    database.createTable(conn)
    
    url = getURL(searchKey)
    res = requests.get(url, verify=False)
    soup = BeautifulSoup(res.content, 'html.parser')
    
    objarray = []
    fillObjArray(soup, objarray)
    
    # Clear the listbox before displaying new results
    listbox.delete(0, tk.END)
    
    # Display the books in the listbox
    for i, book in enumerate(objarray):
        book_info = (
            f"Title: {book['Title']}\n"
            f"Author: {book['Author']}\n"
            f"Publisher: {book['Publisher']}\n"
            f"Year: {book['Year']}\n"
            f"Language: {book['language']}\n"
            f"Pages: {book['pages']}\n"
            f"Size: {book['size']}\n"
            f"Type: {book['Extension']}\n"
            f"---------------------------------\n"
        )
        listbox.insert(tk.END, f"Book {i+1}:")
        listbox.insert(tk.END, book_info)
    
    book_choice = simpledialog.askinteger("Download", "Enter the book number to download (-1 to exit):")
    if book_choice == -1:
        return

    downloadBook(conn, objarray[book_choice - 1])

    conn.close()

