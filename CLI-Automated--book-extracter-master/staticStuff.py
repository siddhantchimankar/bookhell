
from apistuff import apisearch

book = {
    "Title": "None",
    "Author": "None",
    "Publisher": "None",
    "Year": "None",
    "language": "None",
    "size": "None",
    "pages": "None",
    "Extension": "None",
    "imageurl": "None",
    "downloadlink": "None"
}


def fillObjArray(soup, objarray, size):

    for i in soup.findAll('tbody'):
        if(i.parent.parent.name == "font"):
            size = size + 1

            book = {
                "Title": i.find('td', attrs={"colspan": "2"}).text,

                "Author": i.find('td', attrs={"colspan": "3"}).text,

                "Publisher": i.find('font', string="Publisher:").find_next('td').text,

                "Year": i.find('font', string="Year:").find_next('td').text,

                "language": i.find('font', string="Language:").find_next('td').text,

                "size": i.find('font', string="Size:").find_next('td').text,

                "pages": i.find('font', string="Pages:").find_next('td').text,

                "Extension": i.find('font', string="Extension:").find_next('td').text,

                "imageurl": 'http://93.174.95.29/' + i.find('img')["src"],

                "downloadlink": 'https://libgen.is' + i.find('img', attrs={"alt": "Download"}).find_previous('a')["href"]
            }

            objarray.append(book)


def display(objarray, booknum) :

    for i in range(0, min(6, len(objarray))):

        print('---------------------------------\n')

        print('Book No. ' + str(booknum) + ')')

        print('\n')

        print('Title :- ' + objarray[i]["Title"])

        print('Author :- ' + objarray[i]["Author"])

        apisearch(objarray[i]["Title"])

        print('Publisher :- ' + objarray[i]["Publisher"])

        print('\n')

        print('Pages :- ' + objarray[i]["pages"])

        print('Size :- ' + objarray[i]["size"])

        print('Type :- ' + objarray[i]["Extension"])

        print('\n---------------------------------\n')

        booknum = booknum + 1
