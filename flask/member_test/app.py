from flask import Flask, session
from flask.globals import request
from flask.helpers import url_for
from flask.templating import render_template
from flask import jsonify
import pymysql
from werkzeug.utils import redirect
import os

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/form")
def formTest():
    return render_template("form.html")


@app.route("/usersform", methods=["POST", "GET"])
def usersform():
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="qwer1234",
        db="test",
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor,
    )
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
        user = [userid, userpw, username, userage, usermail, useradd, usergender, usertel]
        try:
            with conn.cursor() as cursor:
                sql = """
                insert into users values
                    (%s,%s,%s,%s,%s,%s,%s,%s)
                """
                cursor.execute(sql, user)
                conn.commit()
        finally:
            conn.close()

        return redirect("/")


@app.route("/list")
def list():
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="qwer1234",
        db="test",
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor,
    )
    try:
        with conn.cursor() as cursor:
            sql = """
            select * from users
            """
            cursor.execute(sql)
            result = cursor.fetchall()
            conn.commit()
    finally:
        conn.close()

    return render_template("list.html", list=result)


@app.route("/content/<userid>")
def content(userid):
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="qwer1234",
        db="test",
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor,
    )
    try:
        with conn.cursor() as cursor:
            sql = """
            select * from users where userid = %s
            """
            cursor.execute(sql, userid)
            result = cursor.fetchone()
            conn.commit()
    finally:
        conn.close()

    return render_template("content.html", list=result)


@app.route("/update/<userid>", methods=["GET", "POST"])
def update(userid):
    if request.method == "GET":
        conn = pymysql.connect(
            host="localhost",
            user="root",
            password="qwer1234",
            db="test",
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor,
        )
        try:
            with conn.cursor() as cursor:
                sql = """
                select * from users where userid = %s
                """
                cursor.execute(sql, userid)
                result = cursor.fetchone()
                conn.commit()
        finally:
            conn.close()
        return render_template("updateform.html", list=result)

    elif request.method == "POST":
        conn = pymysql.connect(
            host="localhost",
            user="root",
            password="qwer1234",
            db="test",
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor,
        )
        try:
            with conn.cursor() as cursor:
                sql = """
                UPDATE users set 
                userpw=%s,
                username=%s,
                userage=%s,
                usermail=%s,
                useradd=%s,
                usergender=%s, 
                usertel=%s
                where userid = %s
                """
                userid = request.form.get("userid")
                userpw = request.form.get("userpw")
                username = request.form.get("username")
                userage = request.form.get("userage")
                usermail = request.form.get("usermail")
                useradd = request.form.get("useradd")
                usergender = request.form.get("usergender")
                usertel = request.form.get("usertel")
                user = [
                    userpw,
                    username,
                    userage,
                    usermail,
                    useradd,
                    usergender,
                    usertel,
                    userid,
                ]
                cursor.execute(sql, user)
                conn.commit()
        finally:
            conn.close()
        return redirect(url_for("list"))


@app.route("/delete/<userid>")
def delete(userid):
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="qwer1234",
        db="test",
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor,
    )
    try:
        with conn.cursor() as cursor:
            sql = """
            delete from users where userid = %s
            """
            cursor.execute(sql, userid)
            conn.commit()
    finally:
        conn.close()
    return redirect(url_for("list"))


@app.route("/ajaxlist", methods=["GET", "POST"])
def ajaxlist():
    if request.method == "GET":
        conn = pymysql.connect(
            host="localhost",
            user="root",
            password="qwer1234",
            db="test",
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor,
        )
        try:
            with conn.cursor() as cursor:
                sql = """
                select * from users
                """
                cursor.execute(sql)
                result = cursor.fetchall()
                conn.commit()
        finally:
            conn.close()

        return render_template("ajaxlist.html", list=result)

    elif request.method == "POST":
        userid = request.form.get("userid")
        conn = pymysql.connect(
            host="localhost",
            user="root",
            password="qwer1234",
            db="test",
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor,
        )
        if userid == "":
            try:
                with conn.cursor() as cursor:
                    sql = """
                    select * from users 
                    """
                    cursor.execute(sql)
                    result = cursor.fetchall()
                    conn.commit()
            finally:
                conn.close()
            return jsonify(result)

        else:
            try:
                with conn.cursor() as cursor:
                    sql = """
                    select * from users where userid LIKE %s
                    """
                    userid = "%" + userid + "%"
                    cursor.execute(sql, userid)
                    result = cursor.fetchall()
                    conn.commit()
            finally:
                conn.close()

            return jsonify(result)


@app.route("/imglist")
def imglist():
    print(os.path.dirname(__file__))
    dirname = os.path.dirname(__file__) + "/static/img/"
    filenames = os.listdir(dirname)
    return render_template("imglist.html", filenames=filenames)


if __name__ == "__main__":
    app.run(debug=True, port=8089)

