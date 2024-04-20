#!/usr/bin/python3
"""Module that starts a Flask web app
"""
from models import storage
from models.city import City
from models.state import State
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    all_states = storage.all(State).values()
    return render_template('9-states.html', states=all_states, cities=0)


@app.route('/states/<id>', strict_slashes=False)
def states_by_id(id=None):
    all_states = storage.all(State).values()
    selected_s = list(filter(lambda x: x.id == id, all_states))
    if len(selected_s) == 0:
        selected_s = None
    else:
        selected_s = selected_s[0]
    return render_template("9-states.html", states=selected_s, cities=1)


@app.teardown_appcontext
def tear_down(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
