import numpy as np
import pandas as pd
from time import time
from warnings import warn
from time import sleep
from IPython.core.display import clear_output


import requests
from bs4 import BeautifulSoup
import urllib


import itertools

while True :

    baseurl = 'https://libgen.is/search.php?req=&open=0&res=25&view=detailed&phrase=0&column=def'

    searchOption = 0
    searchOption = int(input('Search by Book Name --> Press 1\nSearch by Author Name --> Press 2\nExit --> Press 3\n'))

    if(searchOption != 3):
        if(searchOption == 1):
            bookName = str(input('Enter name of the Book : -\n'))
            bookName = bookName.split(' ')

            #programming the query
            
            query = ''

            for i in range(0, len(bookName)):
                query += bookName[i]
                query += '+'

            query = query[:-1]
            baseurl = baseurl.split('?req=')
            baseurl[0] += '?req='
            baseurl[0] += query
            url = (baseurl[0] + baseurl[1])

            #fetching GET response & parsing its html

            res = requests.get(url)
            soup = BeautifulSoup(res.content, 'html.parser')

            size = 0
            objarray = []            

            #creating book object array

            book = {
                "Title" : "None",
                "Author" : "None",
                "Publisher" : "None",
                "Year" : "None",
                "language" : "None",
                "size" : "None",
                "pages" : "None",
                "Extension" : "None",
                "imageurl" : "None",
                "downloadlink" : "None"
            }

            #populating book object array

            for i in soup.findAll('tbody') :
                if(i.parent.parent.name == "font") :
                    size = size + 1

                    book = {
                        "Title": i.find('td', attrs = {"colspan" : "2"}).text,

                        "Author": i.find('td', attrs={"colspan": "3"}).text,

                        "Publisher": i.find('font', string = "Publisher:").find_next('td').text,

                        "Year": i.find('font', string="Year:").find_next('td').text,

                        "language": i.find('font', string="Language:").find_next('td').text,

                        "size": i.find('font', string="Size:").find_next('td').text,

                        "pages": i.find('font', string="Pages:").find_next('td').text,

                        "Extension": i.find('font', string="Extension:").find_next('td').text,

                        "imageurl": 'http://93.174.95.29/' + i.find('img')["src"],

                        #https://libgen.is/get?&md5=12D8EB50DBE241E6C824FA1F2B748883

                        "downloadlink": 'https://libgen.is' + i.find('img', attrs={"alt": "Download"}).find_previous('a')["href"]
                    }

                    objarray.append(book)


            # for i in objarray :
            #     print(i)
            #     print('\n')


            dic = {}
            for i in range(0, size):
                dic[i] = "None"


            for i in range(0, size):
                dic[i] = objarray[i]["downloadlink"]


            # for i in dic:
            #     print(str(i) + ' ' + str(dic[i]))

            #printing book object array's attributes

            booknum = 0

            if(size >= 5) :

                print('\nHere are the top 5 results - \n')

                for i in itertools.islice(objarray, 0, 5):

                    print('---------------------------------\n')

                    print('Book No. ' + str(booknum) + ')')

                    print('\n')

                    print('Title :- ' + i["Title"])

                    print('Author :- ' + i["Author"])

                    print('Publisher :- ' + i["Publisher"])

                    print('\n')

                    print('Language :- ' + i["language"])

                    print('Pages :- ' + i["pages"])

                    print('Size :- ' + i["size"])

                    print('\n')

                    print('Year :- ' + i["Year"])

                    print('Extension :- ' + i["Extension"])

                    print('Image URL :- ' + i["imageurl"])

                    # print('Download :- ' + i['downloadlink'])

                    print('\n---------------------------------\n')
                    booknum = booknum + 1


                more = 0
                more = str(input('Press M to view all the results otherwise press any other key\n'))

                if(more == 'm'):

                    print('\nHere are the top complete results - \n')

                    for i in objarray:

                        print('---------------------------------\n')

                        print('Book No. ' + str(booknum) + ')')

                        print('\n')

                        print('Title :- ' + i["Title"])

                        print('Author :- ' + i["Author"])

                        print('Publisher :- ' + i["Publisher"])

                        print('\n')

                        print('Language :- ' + i["language"])

                        print('Pages :- ' + i["pages"])

                        print('Size :- ' + i["size"])

                        print('\n')

                        print('Year :- ' + i["Year"])

                        print('Extension :- ' + i["Extension"])

                        print('Image URL :- ' + i["imageurl"])

                        print('\n---------------------------------\n')
                        booknum = booknum + 1


                
                downnum = int(input('Enter Book No. to download book otherwise enter -1-\n'))

                if(downnum != -1):
                    downlink = dic[downnum]

                    downpage = requests.get(downlink)

                    dsoup = BeautifulSoup(downpage.content, 'html.parser')

                    dlink = dsoup.find('a', string="GET")["href"]

                    fl = requests.get(dlink)

                    with open(str(objarray[downnum]['Title']) + '.pdf', 'wb') as f:
                        f.write(fl.content)

                    print(str(objarray[downnum]['Title']) +
                        " is downloaded in the script's folder!\n")



            elif(size < 5 and size > 0):

                print('\nWe found ' + str(size) + ' results -\n')

                for i in objarray:

                    print('---------------------------------\n')

                    print('Book No. ' + str(booknum) + ')')

                    print('\n')

                    print('Title :- ' + i["Title"])

                    print('Author :- ' + i["Author"])

                    print('Publisher :- ' + i["Publisher"])

                    print('\n')

                    print('Language :- ' + i["language"])

                    print('Pages :- ' + i["pages"])

                    print('Size :- ' + i["size"])

                    print('\n')

                    print('Year :- ' + i["Year"])

                    print('Extension :- ' + i["Extension"])

                    print('Image URL :- ' + i["imageurl"])

                    print('\n---------------------------------\n')
                    booknum = booknum + 1


                downnum = int(input('Enter Book No. to download book otherwise enter -1-\n'))

                if(downnum != -1):
                    downlink = dic[downnum]

                    downpage = requests.get(downlink)

                    dsoup = BeautifulSoup(downpage.content, 'html.parser')

                    dlink = dsoup.find('a', string="GET")["href"]

                    fl = requests.get(dlink)

                    with open(str(objarray[downnum]['Title']) + '.pdf', 'wb') as f:
                        f.write(fl.content)

                    print(str(objarray[downnum]['Title']) +
                        " is downloaded in the script's folder!\n")

            elif(size == 0) : 

                print('\nSorry! No results were found\n')
            
            

        else:
            authorName = str(input('Enter Author name : -\n'))
            authorName = authorName.split(' ')

            query = ''

            for i in range(0, len(authorName)):
                query += authorName[i]
                query += '+'

            query = query[:-1]
            baseurl = baseurl.split('?req=')
            baseurl[0] += '?req='
            baseurl[0] += query
            url = (baseurl[0] + baseurl[1])

            #fetching GET response & parsing its html

            res = requests.get(url)
            soup = BeautifulSoup(res.content, 'html.parser')

            size = 0
            objarray = []

            #creating book object array

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

            #populating book object array

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

                        #https://libgen.is/get?&md5=12D8EB50DBE241E6C824FA1F2B748883

                        "downloadlink": 'https://libgen.is' + i.find('img', attrs={"alt": "Download"}).find_previous('a')["href"]
                    }

                    objarray.append(book)

            # for i in objarray :
            #     print(i)
            #     print('\n')

            dic = {}
            for i in range(0, size):
                dic[i] = "None"

            for i in range(0, size):
                dic[i] = objarray[i]["downloadlink"]

            # for i in dic:
            #     print(str(i) + ' ' + str(dic[i]))

            #printing book object array's attributes

            booknum = 0

            if(size >= 5):

                print('\nHere are the top 5 results - \n')

                for i in itertools.islice(objarray, 0, 5):

                    print('---------------------------------\n')

                    print('Book No. ' + str(booknum) + ')')


                    print('\n')

                    print('Title :- ' + i["Title"])

                    print('Author :- ' + i["Author"])

                    print('Publisher :- ' + i["Publisher"])

                    print('\n')

                    print('Language :- ' + i["language"])

                    print('Pages :- ' + i["pages"])

                    print('Size :- ' + i["size"])

                    print('\n')

                    print('Year :- ' + i["Year"])

                    print('Extension :- ' + i["Extension"])

                    print('Image URL :- ' + i["imageurl"])

                    # print('Download :- ' + i['downloadlink'])

                    print('\n---------------------------------\n')
                    booknum = booknum + 1

                more = 0
                more = str(
                    input('Press M to view all the results otherwise press any other key\n'))

                if(more == 'm'):

                    print('\nHere are the top complete results - \n')

                    for i in objarray:

                        print('---------------------------------\n')

                        print('Book No. ' + str(booknum) + ')')

                        print('\n')

                        print('Title :- ' + i["Title"])

                        print('Author :- ' + i["Author"])

                        print('Publisher :- ' + i["Publisher"])

                        print('\n')

                        print('Language :- ' + i["language"])

                        print('Pages :- ' + i["pages"])

                        print('Size :- ' + i["size"])

                        print('\n')

                        print('Year :- ' + i["Year"])

                        print('Extension :- ' + i["Extension"])

                        print('Image URL :- ' + i["imageurl"])

                        print('\n---------------------------------\n')
                        booknum = booknum + 1


                downnum = int(input('Enter Book No. to download book otherwise enter -1-\n'))

                if(downnum != -1):
                    downlink = dic[downnum]

                    downpage = requests.get(downlink)

                    dsoup = BeautifulSoup(downpage.content, 'html.parser')

                    dlink = dsoup.find('a', string="GET")["href"]

                    fl = requests.get(dlink)

                    with open(str(objarray[downnum]['Title']) + '.pdf', 'wb') as f:
                        f.write(fl.content)

                    print(str(objarray[downnum]['Title']) +
                        " is downloaded in the script's folder!\n")


            elif(size < 5 and size > 0):

                print('\nWe found ' + str(size) + ' results -\n')

                for i in objarray:

                    print('---------------------------------\n')

                    print('Book No. ' + str(booknum) + ')')

                    print('\n')

                    print('Title :- ' + i["Title"])

                    print('Author :- ' + i["Author"])

                    print('Publisher :- ' + i["Publisher"])

                    print('\n')

                    print('Language :- ' + i["language"])

                    print('Pages :- ' + i["pages"])

                    print('Size :- ' + i["size"])

                    print('\n')

                    print('Year :- ' + i["Year"])

                    print('Extension :- ' + i["Extension"])

                    print('Image URL :- ' + i["imageurl"])

                    print('\n---------------------------------\n')
                    booknum = booknum + 1


                downnum = int(input('Enter Book No. to download book otherwise enter -1-\n'))

                if(downnum != -1):
                    downlink = dic[downnum]

                    downpage = requests.get(downlink)

                    dsoup = BeautifulSoup(downpage.content, 'html.parser')

                    dlink = dsoup.find('a', string="GET")["href"]

                    fl = requests.get(dlink)

                    with open(str(objarray[downnum]['Title']) + '.pdf', 'wb') as f:
                        f.write(fl.content)

                    print(str(objarray[downnum]['Title']) +
                        " is downloaded in the script's folder!\n")

            elif(size == 0):

                print('\nSorry! No results were found\n')



            

    else:
        break
