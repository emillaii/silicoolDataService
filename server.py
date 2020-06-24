from flask import Flask
from flask_restful import Api, Resource, reqparse
from websocket import create_connection

from EAP.EQPStatusReport  import statusReport
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
        
#define route
api.add_resource(User, "/user/<string:name>")
api.add_resource(StatusReport, "/statusReport")

#Run api server
app.run(host="0.0.0.0", debug=False)


