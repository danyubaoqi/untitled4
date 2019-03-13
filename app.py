from flask import Flask, render_template, jsonify, url_for
from flask import request, session, redirect

app = Flask(__name__)
app.secret_key = "super secret key"

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@/mydata'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        user = request.form["user"]
        session["user"] = user
        return render_template("room.html", user=user)
    else:
        if "user" in session:
            return redirect("/room")
        else:
            return render_template("login.html")


@app.route('/room')
def room():
    return render_template("room.html", user=session["user"])


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/logout')
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))


if __name__ == '__main__':
    app.config.from_object("config.debug")
    app.run(host="0.0.0.0", port=5000)
