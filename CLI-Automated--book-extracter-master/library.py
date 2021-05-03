
import database        

def checkLibrary() :
        
    res = []
    conn = database.connect()
    database.createTable(conn)

    choice = int(input('Get All Books --> Press 1\nSearch \
         Book by Title --> Press 2\nSearch Book by Author --> Press 3\n'))

    if choice == 1 :
        
        res = []
        res = database.getAllBooks(conn)

    elif choice == 2:
        
        res = []
        title = input('Enter title : \n')
        res = database.getByTitle(conn, title)

    elif choice == 3 :
        
        res = []
        author = input('Enter title : \n')
        res = database.getByAuthor(conn, author)

    for i in range(0, len(res)) :

        print(res[i])






