from flask import Flask, render_template, request, jsonify
from opinion_books import opinion_books


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process():
    topics = request.form["topics"]
    topics_array = topics.split(",")
    data = opinion_books(1, 2, topics_array)

    return data


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)