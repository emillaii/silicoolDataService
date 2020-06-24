from flask import Flask
from flask_restful import Api, Resource, reqparse
from websocket import create_connection

#Let see whether we need a websocket connection
#ws = create_connection("ws://localhost:19997", origin = "Silicool_Server")

app = Flask(__name__)
api = Api(app)

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
            #ws.send(user["name"])
            print("Receiving")
            #result = ws.recv()
            #print("Received '%s'" %s)
            if(name == user["name"]):
                return user, 200
        return "User not found", 404
    
api.add_resource(User, "/user/<string:name>")
app.run(host="0.0.0.0", debug=False)