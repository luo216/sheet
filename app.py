from data import update
from flask import Flask, jsonify, render_template

app = Flask(__name__)


@app.route("/")
def index():
    data = update()
    return render_template("index.html", data=data)


@app.route("/data")
def get_data():
    data = {
        "title": {"text": "ECharts 入门示例"},
        "tooltip": {},
        "legend": {"data": ["销量"]},
        "xAxis": {"data": ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]},
        "yAxis": {},
        "series": [{"name": "销量", "type": "bar", "data": [5, 20, 36, 10, 10, 20]}],
    }
    return jsonify(data)


@app.route("/data1")
def get_data1():
    data = {
        "title": {"text": "ECharts 入门示例22222222"},
        "tooltip": {},
        "legend": {"data": ["销量"]},
        "xAxis": {"data": ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]},
        "yAxis": {},
        "series": [{"name": "销量", "type": "bar", "data": [5, 20, 36, 10, 10, 20]}],
    }
    return jsonify(data)


if __name__ == "__main__":
    app.run()
