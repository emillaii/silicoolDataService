from datetime import datetime
from Config import Config

template = {
    "eqpId": Config.eqpId,
    "eqpName": Config.eqpName,
    "eqpNumber": Config.eqpNumber,
    "eqpType": Config.eqpType,
    "eqpModel": Config.eqpModel,
    "vendor": Config.vendor,
    "IP": "",
    "computerName": Config.computerName,
    "port": Config.port,
    "FAB": Config.FAB,
    "floor": Config.floor,
    "workshopId": Config.workshopId,
    "department": Config.department,
    "keShi": Config.keShi,
    "position": Config.position,
    "productionLineId": Config.productionLineId,
    "resourceId": Config.resourceId,
    "description": "description",
    "operation": "operation",
    "station": "station",
    "responsible": Config.responsible,
    "createTime": "",
    "operating": "操作说明",
    "macAddress": "mac"
}

def mainInfoReport():
    print("mainInfoReport")
    return template