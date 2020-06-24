from datetime import datetime
from Config import Config

template = {
    "eqpId": Config.eqpId,
    "eventID": "00",
    "eventDesc": "事件描述",
    "eventTime": "2020-01-03 08:12:12.123",
    "orderID": "order ID",
    "ProductID": "产品 ID",
    "StationID": "设备工位",
    "paramList": []
}

paramTemplate = {
    "name": "param001",
    "remark": "remark001",
    "value": "value001"
}

def eventReport():
    print("eventReport")
    return template