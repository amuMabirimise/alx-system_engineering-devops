#!/usr/bin/python3
"""
Scripting that, using a given REST API, for a given employee ID,
returns information about his/her TODO list progress and exports it to JSON.
"""

import requests
import json
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

        employee_id = user_data.get("id")
        employee_username = user_data.get("username")
        json_filename = "{}.json".format(employee_id)

        json_data = {str(employee_id): [{"task": task["title"], "completed": task["completed"], "username": employee_username} for task in todos_data]}

        with open(json_filename, mode='w') as json_file:
            json.dump(json_data, json_file, indent=4)

        print("Data exported to {}".format(json_filename))

    except requests.exceptions.RequestException as e:
        print("Error: {}".format(e))
        exit(1)
