
from findBook import findBook
from library import checkLibrary

# Main Loop

while True:

    searchOption = int(input(
        'Add new Book --> Press 1\nCheck Your Library --> Press 2\nExit --> Press 3\n'))

    if searchOption == 3:
        break

    if(searchOption == 1):
        findBook()

    if(searchOption == 2):
        checkLibrary()
