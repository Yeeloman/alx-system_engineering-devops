#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users"
    user = requests.get(url + f"/{sys.argv[1]}")
    todos = requests.get(url + f"/{sys.argv[1]}" + "/todos")
    total = 0
    comp = 0
    for el in todos.json():
        if el['completed'] is True:
            comp += 1
        total += 1

    print("Employee {} is done with tasks({}/{}):".format(
        user.json()['name'], comp, total))
    for el in todos.json():
        if el['completed'] is True:
            print("\t" + " " + f"{el['title']}")
