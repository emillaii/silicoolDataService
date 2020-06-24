from datetime import datetime

template = {
    "eqpId": "Silicool Machine 1",
    "runStatus": 1,
    "eqpType": "AA",
    "collectionTime": "2020-01-02 08:17:12.123456",
    "position": "Sunny",
    "description": "......",
    "lotNo": "12345",
    "orderNo": "order 1234",
    "uph": 400,
    "qty": 1090,
    "doneQty": 1000,
    "defectQty": 19,
    "recipeid": "AS2018N",
    "startTime": "2020-01-02 08:17:12.123456",
    "alarmCode": "EC2008",
    "alarmStatus": "set"
}

def statusReport():
    print("StatusReport")
    #ToDo Sync with Machine or load the object in cache
    now = datetime.now()
    dt_string = now.strftime("%Y-%M-%d %H:%M:%S.%f")
    template["collectionTime"] = dt_string
    return template