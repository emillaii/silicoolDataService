from datetime import datetime
from Config import Config
from EQPDataCollectionReport import getCachedResult 

def getEQPParameterList(req):
    if req.get('eqpId'):
       print(req['eqpId'])
       return getCachedResult()
    else:
        return 'Invalid Input! Missing eqpId'