#!/usr/bin/python3
"""Script that, using a REST API, for a given employee ID,
returns, in a JSON file, information about his/her TODO list progress
"""
import json
import requests
import sys


if __name__ == '__main__':
    user_id = int(sys.argv[1])

    # Get the user's name:
    url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    response = requests.get(url)
    user = response.json()
    username = user.get('username')

    # Filter user todos:
    response = requests.get('https://jsonplaceholder.typicode.com/todos/')
    todos = response.json()
    user_tasks = [task for task in todos if task.get('userId') == user_id]

    tasks_list = []
    for task in user_tasks:
        entry = {'task': task.get('title'), 'completed': task.get('completed'),
                 'username': username}
        tasks_list.append(entry)

    user_dict = {f'{user_id}': tasks_list}

    # Write user_dict to a JSON file:
    with open(f'{user_id}.json', 'w') as file:
        json.dump(user_dict, file)
