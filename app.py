from data import keywords, get_date
from flask import Flask, jsonify, render_template

app = Flask(__name__)


@app.route("/")
def index():
    data = keywords()
    return render_template("index.html", data=data)


@app.route("/data/<index>", methods=["GET"])
def handle_data(index):
    index = int(index)
    data = {}
    get_date(data, index)
    return jsonify(data)


if __name__ == "__main__":
    app.run()
