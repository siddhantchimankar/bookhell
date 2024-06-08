
# from findBook import findBook
# from library import checkLibrary

# # Main Loop

# while True:

#     searchOption = int(input(
#         'Add new Book --> Press 1\nCheck Your Library --> Press 2\nExit --> Press 3\n'))

#     if searchOption == 3:
#         break

#     if(searchOption == 1):
#         findBook()

#     if(searchOption == 2):
#         checkLibrary()



import tkinter as tk
from findBook import findBook
from library import checkLibrary

class LibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Shellbook")

        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20)

        self.label = tk.Label(self.frame, text="Shellbook", font=("Arial", 20))
        self.label.pack(pady=10)

        self.search_frame = tk.Frame(self.frame)
        self.search_frame.pack(pady=10)

        self.search_label = tk.Label(self.search_frame, text="Enter search keyword:")
        self.search_label.pack(side=tk.LEFT)

        self.search_entry = tk.Entry(self.search_frame)
        self.search_entry.pack(side=tk.LEFT)

        self.search_button = tk.Button(self.frame, text="Find Book", command=self.findBook)
        self.search_button.pack(pady=10)

        self.library_button = tk.Button(self.frame, text="Check Your Library", command=self.checkLibrary)
        self.library_button.pack(pady=10)

        self.exit_button = tk.Button(self.frame, text="Exit", command=self.root.quit)
        self.exit_button.pack(pady=10)

        self.result_frame = tk.Frame(self.frame)
        self.result_frame.pack(pady=20)

        self.result_listbox = tk.Listbox(self.result_frame, width=100, height=20)
        self.result_listbox.pack(side=tk.LEFT)

        self.scrollbar = tk.Scrollbar(self.result_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.result_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.result_listbox.yview)

    def findBook(self):
        keyword = self.search_entry.get()
        findBook(keyword, self.result_listbox)

    def checkLibrary(self):
        checkLibrary(self.result_listbox)

# Main Tkinter app
root = tk.Tk()
app = LibraryApp(root)
root.mainloop()
