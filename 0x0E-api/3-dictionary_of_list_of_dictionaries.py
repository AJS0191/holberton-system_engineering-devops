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
            employeeDict.update({n:dic})
        n += 1
    #print(employeeDict)
    allTasks = {}
    taskResponse = requests.get(
        'https://jsonplaceholder.typicode.com/todos'
        )
    taskResponseList = taskResponse.json()
    #print(f'-------------------------------------{taskResponseList}----------------------------------')
    for dict in taskResponseList:
            #print('got a match')
            allTasks.update({dict['userId']:dict})

    attrList = []
    newAttrList = []

    for userid, task in allTasks.items():
        tempDic = {"username":employeeDict[userid]['username'],
                   'task':task['title'],
                   "completed":task['completed']
        }
        attrList.append(tempDic)
    efnDic = {}
    for iD, employee in employeeDict.items():
        for task in attrList:
            if employee['username'] == task['username']:
                newAttrList.append(task)
        efnDic.update({iD:newAttrList})
    jsonDic = efnDic
    with open('todo_all_employees.json'.format(argv[1]), 'w', encoding='utf-8') as jsonFile:
        jString = json.dumps(jsonDic)
        jsonFile.write(jString)


if __name__ == '__main__':
    main()
