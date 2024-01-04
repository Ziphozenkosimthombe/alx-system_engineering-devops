#!/usr/bin/python3
"""Script that, using a REST API, for all the employees,
returns, in a JSON file, information about their TODO list progress
"""
import json
import requests


if __name__ == '__main__':
    # Get the user's name:
    url = f'https://jsonplaceholder.typicode.com/users/'
    response = requests.get(url)
    users = response.json()

    dict_of_users_dicts = {}

    for user in users:
        user_id = user.get('id')
        username = user.get('username')

        # Filter user todos:
        url = 'https://jsonplaceholder.typicode.com/todos/'
        response = requests.get(url)
        todos = response.json()
        user_tasks = [task for task in todos if task.get('userId') == user_id]

        tasks_list = []
        for task in user_tasks:
            entry = {'username': username, 'task': task.get('title'),
                     'completed': task.get('completed')}
            tasks_list.append(entry)

        dict_of_users_dicts[f'{user_id}'] = tasks_list

    # Write user_dict to a JSON file:
    with open('todo_all_employees.json', 'w') as file:
        json.dump(dict_of_users_dicts, file)
