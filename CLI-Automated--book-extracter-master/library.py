
# import database        

# def checkLibrary() :
        
#     res = []
#     conn = database.connect()
#     database.createTable(conn)

#     choice = int(input('Get All Books --> Press 1\nSearch \
#          Book by Title --> Press 2\nSearch Book by Author --> Press 3\n'))

#     if choice == 1 :
        
#         res = []
#         res = database.getAllBooks(conn)

#     elif choice == 2:
        
#         res = []
#         title = input('Enter title : \n')
#         res = database.getByTitle(conn, title)

#     elif choice == 3 :
        
#         res = []
#         author = input('Enter title : \n')
#         res = database.getByAuthor(conn, author)

#     for i in range(0, len(res)) :

#         print(res[i])


import tkinter as tk
import database

def checkLibrary(listbox):
    conn = database.connect()
    database.createTable(conn)
    cursor = conn.cursor()
    cursor.execute("SELECT Title, Author, pages FROM bookDB")
    rows = cursor.fetchall()
    
    # Clear the listbox before displaying new results
    listbox.delete(0, tk.END)
    
    for i, row in enumerate(rows):
        book_info = (
            f"Title: {row[0]}\n"
            f"Author: {row[1]}\n"
            f"Pages: {row[2]}\n"
            f"---------------------------------\n"
        )
        listbox.insert(tk.END, f"Book {i+1}:")
        listbox.insert(tk.END, book_info)

    conn.close()





