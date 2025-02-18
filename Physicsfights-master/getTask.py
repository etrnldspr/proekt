﻿import json

def getTask(userid):
    fileObject = open("tasks.json", "r", encoding="UTF-8")
    jsonContent = fileObject.read()
    aList = json.loads(jsonContent)
    taskid=""
    task=""
    ans=""
    for item in aList:
        useridIsSolved=False
        for i1 in item['solved']:
            if i1==userid:
                useridIsSolved=True
                break
        if useridIsSolved==False:
            str1 = item['task']
            ans=item['ans']
            taskid=item['taskid']
            with open(str1, "r", encoding="UTF-8") as file:
                task = file.read()
            break
    return task, ans, taskid

def getScore(userid):
    fileObject = open("tasks.json", "r", encoding="UTF-8")
    jsonContent = fileObject.read()
    aList = json.loads(jsonContent)
    score=0
    for item in aList:
        useridIsSolved=False
        for i1 in item['solved']:
            if i1==userid:
                useridIsSolved=True
                break
        if useridIsSolved:
            score+=item['score']
    return score

def CheckAns(userid,taskid, cans):
    fileObject = open("tasks.json", "r", encoding="UTF-8")
    jsonContent = fileObject.read()
    aList = json.loads(jsonContent)
    for item in aList:
        if taskid==item['taskid']:
            if cans==item['ans']:
                item['solved'].append(userid)
                jsonString = json.dumps(aList, ensure_ascii=False)
                jsonFile = open("tasks.json", "w", encoding="UTF-8")
                jsonFile.write(jsonString)
                jsonFile.close()
                return True
            
    return False


if __name__ == '__main__':
    task, ans, taskid = getTask("123")
    print(task)
    print(ans)
    print(taskid)
    score = getScore("123")
    print(score)
    print(CheckAns("123","2", "14"))
    task, ans, taskid = getTask("123")
    print(task)
    print(ans)
    print(taskid)