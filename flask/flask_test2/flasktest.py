from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/")
def index():

    return render_template("index.html")


@app.route("/method/", methods=["GET", "POST"])
def result():
    if request.method == "GET":
        username = request.args.get("name")
        userpass = request.args.get("pass")

        return "username = %s , userpass = %s" % (username, userpass,)
    else:
        username = request.form["name"]
        userpass = request.form["pass"]
        result = {
            "username": username,
            "userpass": userpass,
        }
        return render_template("result.html", result=result)


if __name__ == "__main__":
    app.run(debug=True, port=8089)

