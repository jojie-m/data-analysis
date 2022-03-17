from flask import Flask
from suncalc import get_position, get_times
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
import requests
import json
import pandas as pd

app = Flask(__name__)


@app.route('/')
def get_datta():
    date = datetime.now()
    lon = 20
    lat = 45
    epoch = 1588704959.321
    orientation = -10.2
    return {'welcome..here is the location of the sun rays to earth.....' 'positions': get_position(date, lon, lat),
            'times': get_times(date, lon, lat)}
