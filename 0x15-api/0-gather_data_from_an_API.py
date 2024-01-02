#!/usr/bin/python3
"""
Scripting that, using a given REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) != 2 or not argv[1].isdigit():
        print("Usage: {} employee_id".format(argv[0]))
        exit(1)

    employee_id = int(argv[1])

    base_url = "https://jsonplaceholder.typicode.com"
    user_url = "{}/users/{}".format(base_url, employee_id)
    todos_url = "{}/todos?userId={}".format(base_url, employee_id)

    try:
        user_response = requests.get(user_url)
        todos_response = requests.get(todos_url)
        user_data = user_response.json()
        todos_data = todos_response.json()

        employee_name = user_data.get("name")
        total_tasks = len(todos_data)
        done_tasks = [task for task in todos_data if task.get("completed")]

        print("Employee {} is done with tasks({}/{}):".format(
            employee_name, len(done_tasks), total_tasks))

        for task in done_tasks:
            print("\t {}".format(task.get("title")))

    except requests.exceptions.RequestException as e:
        print("Error: {}".format(e))
        exit(1)
