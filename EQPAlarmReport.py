from datetime import datetime
from Config import Config

template = {
    "eqpId": Config.eqpId,
    "eqpType": Config.eqpType,
    "alarmMessage" : "Alarm Message",
    "alarmCode" : "Alarm001",
    "alarmStatus": "set",
    "alarmTime": "",
    "position": Config.position
}

def alarmReport():
    print("alarmReport")
    #ToDo Sync with Machine or load the object in cache
    now = datetime.now()
    dt_string = now.strftime("%Y-%M-%d %H:%M:%S.%f")
    template["alarmTime"] = dt_string
    return template