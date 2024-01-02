#!/usr/bin/python3
"""Extending a Python script to export data in JSON format."""
import json
import requests
from sys import argv


def export_to_json(user_id=None):
    """Exporting a data to JSON."""
    api_url = 'https://jsonplaceholder.typicode.com'
    user_endpoint = f'{api_url}/users/{user_id}' if user_id else f'{api_url}/users'
    tasks_endpoint = f'{api_url}/todos'

    try:
        user_response = requests.get(user_endpoint)
        user_data = user_response.json() if user_id else requests.get(user_endpoint).json()

        tasks_response = requests.get(tasks_endpoint)
        tasks_data = tasks_response.json()

        if user_id and not user_data:
            print("No employee found with this ID")
            return

        if user_id:
            user_data = {str(user_id): user_data}
            tasks_data = [task for task in tasks_data if task['userId'] == user_id]

        user_tasks = []
        for task in tasks_data:
            task_info = {
                'username': user_data[0]['username'] if user_id else user_data[task['userId'] - 1]['username'],
                'task': task['title'],
                'completed': task['completed'],
            }
            user_tasks.append(task_info)

        output_data = {str(user_id) if user_id else 'todo_all_employees': user_tasks}

        with open(f"{user_id}.json" if user_id else 'todo_all_employees.json', 'w') as json_file:
            json.dump(output_data, json_file)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(argv) == 2:
        user_id = argv[1]
        export_to_json(user_id)
    else:
        export_to_json()
