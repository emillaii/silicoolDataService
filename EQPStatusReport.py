from datetime import datetime
from Config import Config

class StatusReport:
    report = {
        "eqpId": Config.eqpId,
        "eqpType": Config.eqpType,
        "collectionTime": "2020-01-02 08:17:12.123456",
        "position": Config.position,
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

new_statusReport = StatusReport()

def statusReport():
    print("Retrieve StatusReport")
    return new_statusReport.report

#Update the status report according to the machine post data
def updateStatusReport(body):
    print("Update status report")
    now = datetime.now()
    dt_string = now.strftime("%Y-%M-%d %H:%M:%S.%f")
    body["collectionTime"] = dt_string
    new_statusReport.report = body
    
def getCachedStatus():
    return new_statusReport.report
    