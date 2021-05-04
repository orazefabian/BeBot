from flask import Flask, request
from api import sportAPI as sport

app = Flask(__name__)


@app.route('/')
def welcome_server():
    return 'Bebot server is listening'


@app.route('/update')
def update_stats():
    return sport.update_stats()


@app.route('/predictions')
def load_predictions():
    return sport.load_predictions()


@app.route('/previous')
def load_previous():
    return sport.load_prev_stats()


@app.route('/headtohead')
def get_head_to_head():
    match_id = request.args.get('matchID')
    return sport.get_head_to_head_details(match_id)


if __name__ == '__main__':
    app.run(port=5000)
