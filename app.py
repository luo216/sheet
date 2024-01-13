from data import keywords, get_date
from flask import Flask, jsonify, render_template

app = Flask(__name__)


@app.route("/")
def index():
    data = keywords()
    return render_template("index.html", data=data)


@app.route("/data/<index>", methods=["GET"])
def handle_data(index):
    data = {
        "title": {"text": index},
        "tooltip": {},
        "legend": {"data": ["销量"]},
        "xAxis": {"data": ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]},
        "yAxis": {},
        "series": [{"name": "销量", "type": "bar", "data": [5, 20, 36, 10, 10, 20]}],
    }
    return jsonify(data)


if __name__ == "__main__":
    app.run()
