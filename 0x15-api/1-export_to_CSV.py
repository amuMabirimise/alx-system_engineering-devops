#!/usr/bin/python3
"""
Scripting that, using a given REST API, for a given employee ID,
returns information about his/her TODO list progress and exports it to CSV.
"""

import requests
import csv
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
        employee_name = user_data.get("username")
        csv_filename = "{}.csv".format(employee_id)

        with open(csv_filename, mode='w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
            csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

            for task in todos_data:
                task_completed_status = task.get("completed")
                task_title = task.get("title")
                csv_writer.writerow([employee_id, employee_name, task_completed_status, task_title])

        print("Data exported to {}".format(csv_filename))

    except requests.exceptions.RequestException as e:
        print("Error: {}".format(e))
        exit(1)
