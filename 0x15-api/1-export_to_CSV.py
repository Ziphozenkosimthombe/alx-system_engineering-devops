#!/usr/bin/python3
"""Script that, using a REST API, for a given employee ID,
returns, in a CSV file, information about his/her TODO list progress
"""
import csv
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

    records = []
    for task in user_tasks:
        rec = [user_id, username, task.get('completed'), task.get('title')]
        records.append(rec)

    # Write records to a CSV file:
    with open(f'{user_id}.csv', 'w') as file:
        csv_writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        csv_writer.writerows(records)
