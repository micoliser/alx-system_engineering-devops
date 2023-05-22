#!/usr/bin/python3
"""
    This script uses a REST API, for a given employee ID,
    and exports information about his/her TODO list progress.
"""
if __name__ == "__main__":
    import csv
    import requests
    import sys

    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users"

    res = requests.get("{}/{}".format(url, employee_id))
    employee_name = res.json().get("username")

    res = requests.get("{}/{}/todos".format(url, employee_id))
    tasks = res.json()

    file_name = "{}.csv".format(employee_id)
    with open(file_name, "w", newline="") as csvfile:
        writer = csv.writer(csvfile, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_ALL)

        for task in tasks:
            row = [
                employee_id, employee_name,
                task["completed"], task["title"]
            ]

            writer.writerow(row)
