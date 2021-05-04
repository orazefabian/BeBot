from flask import Flask

app = Flask(__name__)


@app.route("/")
def welcome_server():
    return 'Bebot server is listening'


if __name__ == '__main__':
    app.run(port=5000)
