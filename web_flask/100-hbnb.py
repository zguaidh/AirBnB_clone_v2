#!/usr/bin/python3
"""Module that starts a Flask web app
"""
from models import storage
from models.city import City
from models.state import State
from models.place import Place
from models.amenity import Amenity
from flask import Flask, render_template, url_for


app = Flask(__name__)


def get_data():
    all_city = storage.all(City).values()
    all_state = storage.all(State).values()
    all_place = storage.all(Place).values()
    all_amenity = storage.all(Amenity).values()

    d_dict = {
            'City': all_city,
            'State': all_state,
            'Place': all_place,
            'Amenity': all_amenity
    }
    return d_dict


@app.route('/hbnb', strict_slashes=False)
def hbnb_website():
    d_db = get_data()
    return render_template('100-hbnb.html', data=d_db)


@app.teardown_appcontext
def tear_down(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
