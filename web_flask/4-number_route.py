#!/usr/bin/python3
"""
Creating flask app
"""

from flask import Flask
from markupsafe import escape

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


@app.route("/c/<text>")
def replace_text(text):
    """
    text replacement using variables
    """
    if '_' in text:
        text = text.replace("_", " ")
    return f"C {text}"


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python/", strict_slashes=False)
def python_route(text='is cool'):
    """
    define a route for python path
    """
    if '_' in text:
        text = text.replace("_", " ")
    return f"{escape(f'Python {text}')}"


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    return if it's a number
    """
    return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
