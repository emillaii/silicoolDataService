from datetime import datetime
from Config import Config

template = {
    "eqpId": Config.eqpId
}

def dataTimeRequest():
    print("dataTimeRequest")
    return template