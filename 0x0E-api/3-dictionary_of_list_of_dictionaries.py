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
    n = 1
    #print(apiResponse.json())
    userResponseList = apiResponse.json()
    for dic in userResponseList:
        if n == 1:
            employeeDict = {n:dic}
        else:
            employeeDict[{n:dic}]
        n += 1
    print(employeeDict)
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
    n = 1
'''
for task in allTasks:
        tempDic = {"username":
                   'task':task['title'],
                   "completed":task['completed']
        }
        attrList.append(tempDic)
    #print(attrList)
    jsonDic = {argv[1]:attrList}
    with open('{}.json'.format(argv[1]), 'w', encoding='utf-8') as jsonFile:
        jString = json.dumps(jsonDic)
        jsonFile.write(jString)

'''
if __name__ == '__main__':
    main()
