#!/usr/bin/env python3
"""0. Basic Flask app"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    """render the 0-index.html file"""
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(debug=True, port=9000)
