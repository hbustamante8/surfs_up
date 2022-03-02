from flask import Flask, jsonify
import datetime as dt
import numpy as np
import pandas as pd
import app

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# set up our database engine for the Flask application and query the database file

engine = create_engine("sqlite:///hawaii.sqlite")

# reflect database into our clases
Base = automap_base()

# reflect the database 
Base.prepare(engine, reflect=True)
# save our references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station
#create session link
session = Session(engine)

app = Flask(__name__)
# Build the home route
@app.route("/")
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')

# Create precipitation route and the function 
@app.route("/api/v1.0/precipitation")
def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)

# Create route for stations analysis

@app.route("/api/v1.0/stations")
#function for station analysis query

def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(station=stations)



# create route for temperature observations
@app.route("/api/v1.0/tobs")

# Function to return temperature observations
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

# create route for starting and end date summary statistics for that month
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)

app.run()
