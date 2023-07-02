import csv
import json
import math
from files import BOOKS_FILE_PATH, USERS_FILE_PATH

books_arr = []
with open(BOOKS_FILE_PATH) as my_file:
    reader = csv.DictReader(my_file)
    for i in reader:
        book = { 'title'       : i['Title']
               , 'author'      : i['Author']
               , 'genre'       : i['Genre']
               , 'pages'       : i['Pages']
               , 'publisher'   : i['Publisher']
        }
        books_arr.append(book)

users_json = []
users_arr = []
with open(USERS_FILE_PATH) as my_file:
    users_json = json.load(my_file)

books_to_user = math.ceil(len(books_arr) / len(users_json))

l_indx = 0
for i in users_json:
    users_arr.append({ 'name'      : i['name']
                     , 'gender'    : i['gender']
                     , 'address'   : i['address']
                     , 'age'       : i['age']
                     , 'books'     : []
    })

l_indx = 0
for i in range(books_to_user):
    for j in range(len(users_arr)):
        users_arr[j]['books'].append(books_arr[l_indx])
        l_indx += 1
        if l_indx >= len(books_arr):
            break
    if l_indx >= len(books_arr):
        break
 
with open('result.json', 'w') as my_file:
    json.dump(users_arr, my_file, indent=4)
