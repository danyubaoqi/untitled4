from flask import Flask, template_rendered, jsonify, url_for
import os

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!123123123'


@app.route("/index")
def index():
    return url_for("index.html")


if __name__ == '__main__':
    app.run(port=5000, debug=True)
