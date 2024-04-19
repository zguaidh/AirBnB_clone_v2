#!/usr/bin/python3
"""Module that displays 'Hello HBNB!' when requesting the web
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """Responds with 'Hello HBNB!' when requested
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    if "_" in text:
        text = text.replace("_", " ")
    return f"C {text}"


@app.route('/python/<text>', strict_slashes=False)
def python_is_fun(text):
    if "_" in text:
        text = text.replace("_", " ")
    return f"Python {text}"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
