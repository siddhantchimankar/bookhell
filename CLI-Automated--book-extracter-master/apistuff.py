import requests
import json

def apisearch(title) :

    base_link = "https://www.googleapis.com/books/v1/volumes?q="
    link = base_link + title
    return generate_result(link)

def generate_result(link) :
    response = requests.get(link).json()

    #print(json.dumps(response["items"][0]["volumeInfo"], indent = 8))
    
    try :
        print('Description : ' + response["items"]
              [0]["volumeInfo"]["description"])
    except :
        print("Description Not found in GoogleBooks API")

    try:

        print("Average Rating (GoogleBooks API) : ")

        print(
              response["items"][0]["volumeInfo"]["averageRating"])
    except:
        print("Average Rating Not found in GoogleBooks API")
    
