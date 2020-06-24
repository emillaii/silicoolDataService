from datetime import datetime
from Config import Config

template = {
    "eqpId": Config.eqpId,
    "orderNo": Config.eqpType,
    "collectionTime": "2020-01-02 08:17:12.123456",
    "station": "AA1",
    "parameterType": "test params",
    "paramList": []
}

paramTemplate = {
    "name": "param001",
    "remark": "remark001",
    "value": "value001"
}

def dataCollectionReport():
    print("dataCollectionReport")
    template["paramList"] = [] 
    #ToDo Sync with Machine or load the object in cache
    now = datetime.now()
    dt_string = now.strftime("%Y-%M-%d %H:%M:%S.%f")
    template["collectionTime"] = dt_string
    
    #Generate dummy param list
    paramList1 = paramTemplate.copy()
    paramList2 = paramTemplate.copy()
    paramList2["name"] = "param002"
    paramList2["remark"] = "remark002"
    paramList2["value"] = "value002"
    
    template["paramList"].append(paramList1)    
    template["paramList"].append(paramList2)    
    
    return template