# import json

# data = [
#     {'name' : 'rayhan','phone': '01273479238','email': 'rayhan@gmail.com'},
#     {'name' : 'pranto','phone': '01273479238','email': 'rayhan@gmail.com'},
#     {'name' : 'sajib','phone': '01273479238','email': 'rayhan@gmail.com'}
# ]

# with open('C:/Users/Hp/Desktop/python/file_handling/json/contacts.json' , 'w') as file:
#     json.dump(data, file)

# with open('C:/Users/Hp/Desktop/python/file_handling/json/contacts.json' , 'r') as file:
#     data = json.load(file)
#     # print(data)
#     new_data = {'name': 'raju','phone':'0123342342', 'email' :'raju@gmail.com'}
#     data.append(new_data)
#     # নামগুলো প্রিন্ট করা
#     for contact in data:
#         print(contact['name'])

# import requests

# url = 'https://jsonplaceholder.typicode.com/users'

# response = requests.get(url)

# data = response.json()

# for user in data:
#     print(f"User Name: {user['name']}, User Email: {user['email']}")

import sqlite3

# ডেটাবেসে কানেক্ট হওয়া বা ডেটাবেস তৈরি করা
conn = sqlite3.connect('contacts.db')

# কার্সর তৈরি করা
cursor = conn.cursor()

# টেবিল তৈরি করা
cursor.execute('''
CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY,
    name TEXT,
    phone TEXT,
    email TEXT
)
''')

# পরিবর্তন সেভ করা
conn.commit()

# কানেকশন বন্ধ করা
conn.close()
