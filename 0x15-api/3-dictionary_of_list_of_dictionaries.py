#!/usr/bin/python3
"""
    This script uses a REST API, and exports information about
    all users and TODO list progress.
"""
if __name__ == "__main__":
    import json
    import requests

    url = "https://jsonplaceholder.typicode.com"

    res = requests.get("{}/users".format(url))
    employees = res.json()

    res = requests.get("{}/todos".format(url))
    tasks = res.json()

    employees_dict = {}

    for employee in employees:
        employee_id = employee.get("id")
        task_details = [{
            "username": employee.get("username"),
            "task": task.get("title"),
            "completed": task.get("completed")}
            for task in tasks
            if task.get("userId") == employee_id
        ]

        employees_dict[employee_id] = task_details

    file_name = "todo_all_employees.json"
    with open(file_name, "w", newline="") as f:
        json.dump(employees_dict, f)
