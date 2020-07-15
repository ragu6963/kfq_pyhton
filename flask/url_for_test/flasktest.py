from flask import Flask, redirect
from flask.helpers import url_for

app = Flask(__name__)


@app.route("/admin")
def admin():
    return "hello_admin"


@app.route("/guest/<guest>")
def guest(guest):
    return "hello_%s" % guest


@app.route("/user/<name>")
def user(name):
    if name == "admin":
        return redirect("/admin")
        # return redirect((url_for("admin")))

    else:
        return redirect("/guest/%s" % name)
        # return redirect(url_for("guest", guest=name))


if __name__ == "__main__":
    app.run(debug=True, port=8089)

