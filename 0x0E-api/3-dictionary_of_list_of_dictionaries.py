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
    allTasks = []
    taskResponse = requests.get(
        'https://jsonplaceholder.typicode.com/todos'
        )
    taskResponseList = taskResponse.json()
    #print(f'-------------------------------------{taskResponseList}----------------------------------')
    for dict in taskResponseList:
            allTasks.append(dict)

    jsonDic = {}
    
    for iD, employee in employeeDict.items():
        tempList = []
        for task in allTasks:
            if task['userId'] == iD:
                tempDic = {"username":employee['username'],
                           'task':task['title'],
                           "completed":task['completed']
                }
                tempList.append(tempDic)
        jsonDic.update({iD: tempList})
    
    with open('todo_all_employees.json', 'w', encoding='utf-8') as jsonFile:
        jString = json.dumps(jsonDic)
        jsonFile.write(jString)


if __name__ == '__main__':
    main()
