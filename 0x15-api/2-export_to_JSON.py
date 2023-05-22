#!/usr/bin/python3
"""
    This script uses a REST API, for a given employee ID,
    and exports information about his/her TODO list progress.
"""
if __name__ == "__main__":
    import json
    import requests
    import sys

    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users"

    res = requests.get("{}/{}".format(url, employee_id))
    employee_username = res.json().get("username")

    res = requests.get("{}/{}/todos".format(url, employee_id))
    tasks = res.json()

    task_details = [{
        "task": task.get("title"),
        "completed": task.get("completed"),
        "username": employee_username}
        for task in tasks
    ]
    task_dict = {employee_id: task_details}

    file_name = "{}.json".format(employee_id)
    with open(file_name, "w", newline="") as f:
        json.dump(task_dict, f)
