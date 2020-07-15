from flask import Flask, session
from flask.globals import request
from flask.helpers import url_for
from flask.templating import render_template
from werkzeug.utils import redirect

app = Flask(__name__)


@app.route("/")
def index():
    if "username" in session:
        return "안녕하세요 %s님" % session["username"]

    return "로그인을 하세요"


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        session["username"] = request.form["username"]
        return redirect(url_for("index"))


@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("index"))


app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

if __name__ == "__main__":
    app.run(debug=True, port=8089)

