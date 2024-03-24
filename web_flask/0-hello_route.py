"""
Creating flask app
"""

from flask import Flask, render_template, request

app = Flask(__name__)

app.route("/")
def index():
    """
    return index file
    """
    return ("Hello HBNB")

