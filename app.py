from flask import Flask, render_template, jsonify, url_for
from flask import request, session

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.form=="POST":
        user=request.form["user"]
        session["user"]=user
        return render_template("room.html",user=user)
    else:
        if session["user"]:
            return render_template("room.html",user=session["user"])
        else:return url_for("index")



@app.route('/')
def hello_world():
    return 'Hello World!123123123'


@app.route("/index")
def index():
    return app.send_static_file("index.html")


if __name__ == '__main__':
    app.config.from_object("config.debug")
    app.run(host="0.0.0.0", port=5000)
