from flask import (
    Flask,
    render_template,
    redirect,
    request,
    send_from_directory,
)
import os

UPLOAD_DIRECTORY = os.path.dirname(__file__) + "/files"
if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("main.html")


@app.route("/upload/")
def upload():
    return render_template("upload.html")


@app.route("/fileUpload/", methods=["POST"])
def fileupload():
    f = request.files["file"]
    dirname = os.path.dirname(__file__) + "/files/" + f.filename
    print(dirname)
    f.save(dirname)

    return redirect("/files/")


@app.route("/files/")
def filelist():
    files = []
    for filename in os.listdir(UPLOAD_DIRECTORY):
        path = os.path.join(UPLOAD_DIRECTORY, filename)
        if os.path.isfile(path):
            files.append(filename)

    return render_template("list.html", files=files)


@app.route("/files/<path:path>")
def fileget(path):
    return send_from_directory(UPLOAD_DIRECTORY, path, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True, port=8089)

