from flask import Flask, request
from flask_restful import Api
from api.sportAPI import SoccerStats

app = Flask(__name__)
api = Api(app)


@app.route('/')
def welcome_server():
    return 'Bebot server is listening'


api.add_resource(SoccerStats, '/api/<string:method>')

if __name__ == '__main__':
    app.run(port=5000)
