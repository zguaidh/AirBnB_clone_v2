#!/usr/bin/python3
"""Module that starts a Flask web app
"""
from models import storage
from models.city import City
from models.state import State
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def list_states():
    all_states = storage.all(State).values()
    all_cities = storage.all(City).values()
    sorted_states = sorted(all_states, key=lambda x: x.name)
    sorted_cities = sorted(all_cities, key=lambda x: x.name)
    return render_template('8-cities_by_states.html', states=sorted_states, cities=sorted_cities)


@app.teardown_appcontext
def tear_down(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
