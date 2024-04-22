#!/usr/bin/python3
"""From task 0: Python script to export data in the JSON format"""

import requests
import json
import sys


if __name__ == "__main__":
    Id = int(sys.argv[1])

    user = requests.get('https://jsonplaceholder.typicode.com/users')
    user_data = user.json()

    for u in user_data:
        if u.get('id') == Id:
            name = u.get('username')
            break

    todos = requests.get('https://jsonplaceholder.typicode.com/todos/')
    todo_data = todos.json()

    task_data = []
    for todo in todo_data:
        if todo.get('userId') == Id:
            task = {
                "task": todo.get('title'),
                "completed": todo.get('completed'),
                "username": name
            }
            task_data.append(task)

    file_name = "{}.json".format(Id)
    with open(file_name, 'w') as json_file:
        json.dump({str(Id): task_data}, json_file)
