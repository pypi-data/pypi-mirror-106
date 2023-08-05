from datetime import datetime
import threading
import subprocess
import shortuuid
import os
import time
import re
import pino

logger = pino(bindings={"apptype": "prototype", "context": "main"})

logger.info("Script Scheduler Initializaing")

processIdList = []
runningScript = []
startTimeList = []
endTimeList = []
scriptNameList = []

def scriptRunner(scriptName, startTime, endTime):
    process = subprocess.Popen(["python3", scriptName])
    logger.info("Script --> {} Started Running".format(scriptName))
    return process.pid

def scriptKiller(processId):
    os.system('kill -9 {}'.format(processId))
    logger.info("Process Successfully Stopped Having Process ID --> {}".format(processId))
    return("None",0)

def dataMaker(scriptName, startTime, stopTime):
    for times in startTime:
        startTimeList.append(times)
    for times in stopTime:
        endTimeList.append(times)
    for scriptNames in scriptName:
        scriptNameList.append(scriptNames)

def scriptManager(startTimeList, endTimeList, scriptNameList):
    sTL = len(startTimeList)
    eTL = len(endTimeList)
    sNL = len(scriptNameList)
    print(sNL,sTL, eTL)
    if(sTL != eTL):
        logger.info("Every Start Time Should Have Its End Time")
        return("Every Start Time Should Have Its End Time")
    for i in range(sNL):
        sH, sM = startTimeList[i].split(':')
        eH, eM = endTimeList[i].split(':')
        if datetime.now() >= datetime.now().replace(hour=int(sH), minute=int(sM), second=0, microsecond=0) and datetime.now() <= datetime.now().replace(hour=int(eH), minute=int(eM), second=0, microsecond=0):
            processId = scriptRunner(scriptNameList[i], '{}:{}'.format(int(sH), int(sM)), '{}:{}'.format(int(eH), int(eM)))
            runningScript.append({
                "scriptName": scriptNameList[i],
                "processId": processId,
                "status": '1',
                "startTime": '{}:{}'.format(int(sH), int(sM)),
                "endTime": '{}:{}'.format(int(eH), int(eM)),
                "category": 'started',
                "uuid": shortuuid.uuid()
            })
        else:
            runningScript.append({
                "scriptName": scriptNameList[i],
                "processId": "None",
                "status": '0',
                "startTime": '{}:{}'.format(int(sH), int(sM)),
                "endTime": '{}:{}'.format(int(eH), int(eM)),
                "category": 'stopped',
                "uuid": shortuuid.uuid()
            })
    return("Process Are Configured Sit Back & Relax")

def scriptMonitor(runningScript):
    for items in runningScript:
        scriptName = items['scriptName']
        processId = items['processId']
        status = items['status']
        startTime = items['startTime']
        endTime = items['endTime']
        category = items['category']
        sH, sM = startTime.split(':')
        eH, eM = endTime.split(':')
        if(int(re.findall(r'\d+',str(status))[0]) == 1 and category == 'started'):
            if datetime.now() >= datetime.now().replace(hour=int(sH), minute=int(sM), second=0, microsecond=0) and datetime.now() <= datetime.now().replace(hour=int(eH), minute=int(eM), second=0, microsecond=0):
                print("Status is 1 and Category is started")
            else:
                process_status = scriptKiller(processId)
                items["scriptName"] = scriptName
                items["processId"] = process_status[0]
                items["status"] = str(process_status[1])
                items["startTime"] = '{}:{}'.format(int(sH), int(sM))
                items["endTime"] = '{}:{}'.format(int(eH), int(eM))
                items['category'] = 'stopped'

        elif(int(re.findall(r'\d+',str(status))[0]) == 0 and category == 'stopped'):
            if datetime.now() >= datetime.now().replace(hour=int(sH), minute=int(sM), second=0, microsecond=0) and datetime.now() <= datetime.now().replace(hour=int(eH), minute=int(eM), second=0, microsecond=0):
                processId = scriptRunner(scriptName, '{}:{}'.format(int(sH), int(sM)), '{}:{}'.format(int(eH), int(eM)))
                items["scriptName"] = scriptName
                items["processId"] = processId
                items["status"] = '1'
                items["startTime"] = '{}:{}'.format(int(sH), int(sM))
                items["endTime"] = '{}:{}'.format(int(eH), int(eM))
                items['category'] = 'started'

def scriptScheduler(listOfScripts, listOfStartTimes, listOfEndTimes):
    for script in listOfScripts:
        try:
            if os.path.isfile(script):
                logger.info("File Exists Now Looking For Another If It's In The List")
            else:
                logger.info("{} This File Does Not Look To Be In Place".format(script))
                return("{} This File Does Not Look To Be In Place".format(script))
        except:
            logger.info("Something Went Worng Because Of File --> {}".format(script))
            return("Something Went Worng Because Of File --> {}".format(script))
    dataMaker(listOfScripts, listOfStartTimes, listOfEndTimes)
    time.sleep(5)
    response = scriptManager(startTimeList, endTimeList, scriptNameList)
    if(response == 'Every Start Time Should Have Its End Time'):
        return("Every Start Time Should Have Its End Time")
    else:
        logger.info(response)
    while True:
        scriptMonitor(runningScript)
        logger.info(runningScript)
        time.sleep(20)

def scriptRemove(id):
    global runningScript
    for items in runningScript:
        if(id == items['uuid']):
            items['category'] = 'removed'
            items['status'] = '0'
            scriptKiller(items['processId'])
            items['processId'] = 'None'
    logger.info("Successfully Removed Script From Running Queue")
    return("Successfully Removed Script From Running Queue")

def scriptAdd(id):
    global runningScript
    for items in runningScript:
        if(id == items['uuid']):
            items['category'] = 'stopped'
            items['status'] = '0'
            items['processId'] = 'None'
    logger.info("Successfully Brought Script Back From Queue")
    return("Successfully Brought Script Back From Queue")