from flask import Flask, request
from flask_restful import Api
from api.soccerAPI import Stats

app = Flask(__name__)
api = Api(app)


@app.route('/')
def welcome_server():
    return 'Bebot server is listening'


api.add_resource(Stats, '/api/<string:method>')

if __name__ == '__main__':
    app.run(port=5000)
