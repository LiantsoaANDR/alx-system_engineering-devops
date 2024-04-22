#!/usr/bin/python3
"""
From Task 0:  Python script to export data in the JSON format
Records all tasks from all employees
"""

import json
import requests


if __name__ == "__main__":
    user = requests.get('https://jsonplaceholder.typicode.com/users')
    user_data = user.json()

    todos = requests.get('https://jsonplaceholder.typicode.com/todos/')
    todo_data = todos.json()

    all_tasks = {}
    for u in user_data:
        task_data = []
        for t in todo_data:
            if u.get('id') == t.get('userId'):
                task = {
                        "username": u.get('username'),
                        "task": t.get('title'),
                        "completed": t.get('completed')
                        }
                task_data.append(task)
        all_tasks[str(u.get('id'))] = task_data

    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(all_tasks, json_file)
