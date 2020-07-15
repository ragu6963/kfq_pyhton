from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():

    return render_template("index.html")


@app.route("/cakes")
def cakes():
    return "맛있는 케이크"


# @app.route("/user/<username>")
# def show_user_profile(username):
#     return "%s님 환영합니다" % username


@app.route("/user/<username>/<int:age>")
def show_user_profile(username, age):
    return "%s : %d살" % (username, age)


if __name__ == "__main__":
    app.run(debug=True, port=8089)

