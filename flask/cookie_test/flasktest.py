from flask import Flask, redirect
from flask.globals import request
from flask.helpers import make_response, url_for
from flask.templating import render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/setcookie", methods=["post", "get"])
def setcookie():
    if request.method == "get":
        return render_template("login.html")
    else:
        username = request.form["username"]
        res = make_response("Create Cookies")
        res.set_cookie("username", username)
        return res


@app.route("/getcookie")
def getcookie():
    return request.cookies.get("username")


if __name__ == "__main__":
    app.run(debug=True, port=8089)

