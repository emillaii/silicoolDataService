from flask import Flask
from flask_restful import Api, Resource, reqparse, request
from websocket import create_connection

from EQPStatusReport import statusReport, updateStatusReport
from EQPAlarmReport import alarmReport
from EQPDataCollectionReport import dataCollectionReport
from EQPDataTimeRequest import dataTimeRequest
from EQPMainInfoReport import mainInfoReport
from EQPStartCheck import startCheck
from EQPEventReport import eventReport
from GetEQPParameterList import getEQPParameterList
from GetEQPParameterValueList import getEQPParameterValueList
from GetEQPState import getEQPState
#Let see whether we need a websocket connection
#ws = create_connection("ws://localhost:19997", origin = "Silicool_Server")

app = Flask(__name__)
api = Api(app)
print(statusReport())

users = [
	{
		"name": "Nicholas",
		"age": 42,
		"occupation": "Network Engineer"
	},
	{	"name": "Emil",
		"age": 32,
		"occupation": "Director"
	}
]

class User(Resource):
    def get(self, name):
        for user in users:
            print(user["name"])
            if(name == user["name"]):
                return user, 200
        return "User not found", 404

#define route
api.add_resource(User, "/user/<string:name>")

#Test API for reading the result object
@app.route("/RestAPI/StatusReport", methods=['GET','POST'])
def StatusReport():
    if request.method == 'POST':
        updateStatusReport(request.json)
        return 'OK', 200
    if request.method == 'GET':
        print('Retrieve status report from cache')
    return statusReport(), 200

@app.route("/RestAPI/AlarmReport", methods=['GET','POST'])
def AlarmReport():
    return alarmReport(), 200
    
@app.route("/RestAPI/DataCollectionReport", methods=['GET','POST'])
def DataCollectionReport():
    return dataCollectionReport(), 200
    
@app.route("/RestAPI/DataTimeRequest", methods=['GET','POST'])
def DataTimeRequest():
    return dataTimeRequest(), 200
    
@app.route("/RestAPI/MainInfoReport", methods=['GET','POST'])
def MainInfoReport():
    return mainInfoReport(), 200

@app.route("/RestAPI/StartCheck", methods=['GET','POST'])
def StartCheck():
    return startCheck(), 200

@app.route("/RestAPI/EventReport", methods=['GET','POST'])
def EventReport():
    return eventReport(), 200

#Serve HTTP Post from external party 
@app.route("/RestAPI/GetEQPParameterList", methods=['POST'])
def GetEQPParameterList():
    return getEQPParameterList(request.json), 200

@app.route("/RestAPI/GetEQPParameterValueList", methods=['POST'])
def GetEQPParameterValueList():
    return getEQPParameterValueList(request.json), 200
    
@app.route("/RestAPI/GetEQPState", methods=['POST'])
def GetEQPState():
    return getEQPState(request.json), 200    

@app.route("/RestAPI/CIMMessageCommand", methods=['POST'])
def CIMMessageCommand():
    return 'OK', 200    

@app.route("/RestAPI/DateTimeCommand", methods=['POST'])
def DateTimeCommand():
    return 'OK', 200   

@app.route("/RestAPI/StopEQPCommand", methods=['POST'])
def StopEQPCommand():
    return 'OK', 200        

@app.route("/RestAPI/GetEQPMainInfo", methods=['POST'])
def GetEQPMainInfo():
    return mainInfoReport(), 200    
    

#Run api server
app.run(host="0.0.0.0", debug=False, port=5000)


