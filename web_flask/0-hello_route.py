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


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
