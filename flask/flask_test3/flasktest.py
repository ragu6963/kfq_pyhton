from flask import Flask, render_template, request
import os

# 저장 경로 설정
UPLOAD_DIRECTORY = os.path.dirname(__file__) + "/static/img/"
if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)

app = Flask(__name__)


@app.route("/")
def form():

    return render_template("form.html")


@app.route("/method/", methods=["POST"])
def result():
    f = request.files["pic"]
    dirname = os.path.dirname(__file__) + "/static/img/" + f.filename
    f.save(dirname)
    name = request.form["name"]
    birth = request.form["birth"]
    address = request.form["address"]
    armycondition = request.form["armycondition"]
    email = request.form["email"]

    result = {
        "name": name,
        "birth": birth,
        "address": address,
        "armycondition": armycondition,
        "email": email,
    }
    return render_template("result.html", result=result, pic=f.filename)


if __name__ == "__main__":
    app.run(debug=True, port=8089)

