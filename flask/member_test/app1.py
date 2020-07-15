from flask import Flask, session, jsonify, redirect
from flask.globals import request
from flask.helpers import url_for
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "oracle://hr:hr@127.0.0.1:1521/xe"
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:qwer1234@localhost/test"
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class User(db.Model):
    userid = db.Column(db.String(20), primary_key=True)
    userpw = db.Column(db.String(20))
    username = db.Column(db.String(20))
    userage = db.Column(db.Integer)
    usermail = db.Column(db.String(20))
    useradd = db.Column(db.String(20))
    usergender = db.Column(db.String(20))
    usertel = db.Column(db.String(20))

    def __init__(self, userid, userpw, username, userage, usermail, useradd, usergender, usertel):
        self.userid = userid
        self.userpw = userpw
        self.username = username
        self.userage = userage
        self.usermail = usermail
        self.useradd = useradd
        self.usergender = usergender
        self.usertel = usertel

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/usersform", methods=["POST", "GET"])
def usersform():
    if request.method == "GET":
        return render_template("usersform.html")
    else:
        userid = request.form.get("userid")
        userpw = request.form.get("userpw")
        username = request.form.get("username")
        userage = request.form.get("userage")
        usermail = request.form.get("usermail")
        useradd = request.form.get("useradd")
        usergender = request.form.get("usergender")
        usertel = request.form.get("usertel")
        input_user = User(userid, userpw, username, userage, usermail, useradd, usergender, usertel)
        db.session.add(input_user)
        db.session.commit()
        return redirect("/list")


@app.route("/list")
def list():
    result = User.query.all()
    return render_template("list.html", list=result)


@app.route("/content/<userid>")
def content(userid):
    result = User.query.filter_by(userid=userid).one()
    print(result)
    return render_template("content.html", list=result)


@app.route("/update/<userid>", methods=["GET", "POST"])
def update(userid):
    if request.method == "GET":
        result = User.query.get(userid=userid)
        return render_template("updateform.html", list=result)

    elif request.method == "POST":
        user = User.query.filter_by(userid=userid).one()
        user.userid = request.form.get("userid")
        user.userpw = request.form.get("userpw")
        user.username = request.form.get("username")
        user.userage = request.form.get("userage")
        user.usermail = request.form.get("usermail")
        user.useradd = request.form.get("useradd")
        user.usergender = request.form.get("usergender")
        user.usertel = request.form.get("usertel")
        db.session.commit()
        return redirect(url_for("list"))


@app.route("/delete/<userid>")
def delete(userid):
    user = User.query.get(userid=userid)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for("list"))


@app.route("/ajaxlist", methods=["GET", "POST"])
def ajaxlist():
    if request.method == "GET":
        result = User.query.all()
        return render_template("ajaxlist.html", list=result)

    elif request.method == "POST":
        userid = request.form.get("userid")

        if userid == "":
            result = User.query.all()
            return jsonify(result)
        else:
            query = User.query.filter(User.userid.like("%" + userid + "%")).order_by(User.userid)
            data = query.all()
            result = []
            return jsonify(data)

            for item in data:
                i = {
                    "userid": item.userid,
                    "userpw": item.userpw,
                    "username": item.username,
                    "userage": item.userage,
                    "usermail": item.usermail,
                    "useradd": item.useradd,
                    "usergender": item.usergender,
                    "usertel": item.usertel,
                }
                result.append(i)

            return jsonify(result)


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True, port=8089)

