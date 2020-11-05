from flask import Flask
from flask_restful import Api, Resource, reqparse

from jokes import Jokes
from chat import Chat
from weather import Weather


app = Flask(__name__)
api = Api(app)


api.add_resource(Chat, "/chat")
api.add_resource(Weather, '/weather')
api.add_resource(Jokes, '/jokes')
if __name__ == '__main__':
    app.run(port=45965, debug=True)
