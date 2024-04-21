#!/usr/bin/python3
"""Module that starts a Flask web app
"""
from models import storage
from models.city import City
from models.state import State
from models.amenity import Amenity
from flask import Flask, render_template, url_for


app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def filters():
    a_s = storage.all(State).values()
    a_a = storage.all(Amenity).values()
    return render_template('10-hbnb_filters.html', states=a_s, amenities=a_a)


@app.teardown_appcontext
def tear_down(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
