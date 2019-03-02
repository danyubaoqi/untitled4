from flask import Flask
import os
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!123123123'


if __name__ == '__main__':
    app.run(port= int(os.environ.get('PORT', 5000)))