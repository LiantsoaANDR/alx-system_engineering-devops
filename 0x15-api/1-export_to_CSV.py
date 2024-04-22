#!/usr/bin/python3
"""From task 0,  Python script to export data in the CSV format"""

import csv
import requests
import sys

if __name__ == "__main__":
    Id = int(sys.argv[1])
    user = requests.get('https://jsonplaceholder.typicode.com/users')
    user_data = user.json()
    for i in user_data:
        if i.get('id') == Id:
            name = i.get('name')
            break

    todos = requests.get('https://jsonplaceholder.typicode.com/todos/')
    todo_data = todos.json()
    file_name = "{}.csv".format(Id)

    with open(file_name, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL, lineterminator='\n')
        for data in todo_data:
            if data.get('userId') == Id:
                writer.writerow([Id, name, str(data.get('completed')), data.get('title')])
