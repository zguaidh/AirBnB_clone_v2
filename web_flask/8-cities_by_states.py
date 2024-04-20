#!/usr/bin/python3
"""Module that starts a Flask web app
"""
from models import storage
from models.city import City
from models.state import State
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
@app.route('/cities_by_states/', strict_slashes=False)
def cities_by_states():
    states = storage.all(State).values()
    cities = storage.all(City).values()
    s_s = sorted(states, key=lambda x: x.name)
    s_c = sorted(cities, key=lambda x: x.name)
    return render_template('8-cities_by_states.html', states=s_s, cities=s_c)


@app.teardown_appcontext
def tear_down(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
