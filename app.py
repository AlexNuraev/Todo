
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
# Run server:
# First method: python app.py (app.run needs to be included, like the if statement below)
# Second method: flask run (after exporting 2 env variables:
# export FLASK_ENV=development, export FLASK_APP=app.py)
class Todo():
    def __init__(self, idn, title, complete):
        self.idn = idn
        self.title = title
        self.complete = complete


@app.route('/', methods=["GET"])
def index():
    t = [Todo(123, "Walk the dog", True), Todo(1234, "Walk the dog", True), Todo(12345, "Walk the dog", True)]
    return render_template("index.html", list_todo=t)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
