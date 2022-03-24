#!/usr/bin/python3
"""grabs and displays info from a given API"""

import requests
from sys import argv
import json

def main():
    #employees == users && tasks == todos
    apiResponse = requests.get(
        'https://jsonplaceholder.typicode.com/users'
        )

    print(apiResponse.json())
    userResponseList = apiResponse.json()
    for dict in userResponseList:
        if dict[id] == argv[1]:
            userDict = dict

if __name__ == '__main__':
    main()
