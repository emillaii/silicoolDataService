from flask import Flask
from flask_restful import Api, Resource, reqparse
from websocket import create_connection

from EQPStatusReport import statusReport
from EQPAlarmReport import alarmReport
from EQPDataCollectionReport import dataCollectionReport
from EQPDataTimeRequest import dataTimeRequest
from EQPMainInfoReport import mainInfoReport
from EQPStartCheck import startCheck
from EQPEventReport import eventReport

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

class StatusReport(Resource):
    def get(self):
        return statusReport(), 200

class AlarmReport(Resource):
    def get(self):
        return alarmReport(), 200

class DataCollectionReport(Resource):
    def get(self):
        return dataCollectionReport(), 200
        
class DataTimeRequest(Resource):
    def get(self):
        return dataTimeRequest(), 200

class MainInfoReport(Resource):
    def get(self):
        return mainInfoReport(), 200

class StartCheck(Resource):
    def get(self):
        return startCheck(), 200

class EventReport(Resource):
    def get(self):
        return eventReport(), 200

#define route
api.add_resource(User, "/user/<string:name>")

#Test API for reading the result object
api.add_resource(StatusReport, "/statusReport")
api.add_resource(AlarmReport, "/alarmReport")
api.add_resource(DataCollectionReport, "/dataCollectionReport")
api.add_resource(DataTimeRequest, "/dataTimeRequest")
api.add_resource(MainInfoReport, "/mainInfoReport")
api.add_resource(StartCheck, "/startCheck")
api.add_resource(EventReport, "/eventReport")

#Run api server
app.run(host="0.0.0.0", debug=False, port=5000)


