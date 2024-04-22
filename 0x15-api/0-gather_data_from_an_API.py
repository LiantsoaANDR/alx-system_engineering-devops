#!/usr/bin/python3
"""returns information about his/her TODO list progress"""

import requests
import sys


if __name__ == "__main__":
    Id = int(sys.argv[1])
    user = requests.get('https://jsonplaceholder.typicode.com/users')
    user_data = user.json()
    for i in user_data:
        if i.get('id') == Id:
            name = i.get('name')

    todos = requests.get('https://jsonplaceholder.typicode.com/todos/')
    todo_data = todos.json()
    done = 0
    total = 0
    tasks = []
    for j in todo_data:
        if j.get('userId') == Id:
            total += 1
            if i.get('completed'):
                done += 1
                tasks.append(i.get('title'))

    print("Employee {} is done with tasks({}/{}):".format(name, done, total))

    for k in tasks:
        print("\t {}".format(k))
