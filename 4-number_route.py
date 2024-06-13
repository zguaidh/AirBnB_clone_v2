#!/usr/bin/python3
"""
Module that displays 'Hello HBNB!' when requesting the web
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    if "_" in text:
        text = text.replace("_", " ")
    return f"C {text}"


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_fun(text="is cool"):
    return f"Python {text.replace('_', ' ')}"


@app.route('/number/<int:n>', strict_slashes=False)
def n_is_number(n):
    return f"{n} is a number"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
