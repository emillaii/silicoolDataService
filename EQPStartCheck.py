from datetime import datetime
from Config import Config

template = {
    "eqpId": Config.eqpId,
    "lotNo": "10000"
}

def startCheck():
    print("startCheck")
    return template