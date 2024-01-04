#!/usr/bin/python3
"""Script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress
"""
import requests
import sys


if __name__ == '__main__':
    user_id = int(sys.argv[1])

    # Get the user's name:
    url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    response = requests.get(url)
    user = response.json()
    user_name = user.get('name')

    # Filter and count todos:
    response = requests.get('https://jsonplaceholder.typicode.com/todos/')
    todos = response.json()
    user_tasks = [task for task in todos if task.get('userId') == user_id]
    completed_tasks = [task for task in user_tasks if task.get('completed')]
    print(f'Employee {user_name}',
          f'is done with tasks({len(completed_tasks)}/{len(user_tasks)}):')

    # Print tasks titles:
    for task in completed_tasks:
        task_title = task.get('title')
        print(f'\t {task_title}')
