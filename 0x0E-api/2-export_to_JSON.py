#!/usr/bin/python3
"""grabs and displays info from a given API"""

import json
import os
import requests
from sys import argv

def main():
    """grabs and displays info from a given API1"""
    #employees == users && tasks == todos
    apiResponse = requests.get(
        'https://jsonplaceholder.typicode.com/users'
        )

    #print(apiResponse.json())
    userResponseList = apiResponse.json()
    for dic in userResponseList:
        #print(f'this is type of dict id: {type(dic["id"])}')
        #print(f'this is type of argv[1]: {type(argv[1])}')
        if dic["id"] == int(argv[1]):
            #print(f'Got a match {dic["id"]} {argv[1]}')
            employeeDict = dic
            break
    allTasks = []
    completed = []
    taskResponse = requests.get(
        'https://jsonplaceholder.typicode.com/todos'
        )
    taskResponseList = taskResponse.json()
    for dict in taskResponseList:
        if dict['userId'] == int(argv[1]):
            #print('got a match')
            allTasks.append(dict)
    for task in allTasks:
        if task['completed'] == True:
            completed.append(task)

    attrList = []
    for task in allTasks:
        tempDic = {'task':task['title'],
                   "completed":task['completed'],
                   "username":employeeDict['username']
                   }
        attrList.append(tempDic)
    #print(attrList)
    jsonDic = {argv[1]:attrList}
    with open('{}.json'.format(argv[1]), 'w', encoding='utf-8') as jsonFile:
        jString = json.dumps(jsonDic)
        jsonFile.write(jString)


if __name__ == '__main__':
    main()
