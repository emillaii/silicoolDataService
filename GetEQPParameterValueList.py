from datetime import datetime
from Config import Config
from EQPDataCollectionReport import getCachedResult 

def getEQPParameterValueList(req):
    if req.get('eqpId'):
       print(req['eqpId'])
       cachedResult = getCachedResult()
       returnParamList = []
       if req.get('paramList'):
            for param in req['paramList']:
                for p in cachedResult['paramList']:
                    if p['name'] == param['name']:
                        returnParamList.append(p)
                print(param)
            
       cachedResult['paramList'] = returnParamList
       print(cachedResult["paramList"])
       return cachedResult
    else:
        return 'Invalid Input '