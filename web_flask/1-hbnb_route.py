#!/usr/bin/python3
"""
Creating flask app
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """
    return index file
    """
    return "Hello HBNB!"


@app.route("/hbnb")
def home():
    """
    mapping a url for /hbnb
    """
    return "HBNB"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
