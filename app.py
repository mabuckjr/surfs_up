# import dependencies
import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

# Setup/Access SQLite Database
engine = create_engine("sqlite:///hawaii.sqlite")

# Relect database into the classes
Base = automap_base()

Base.prepare(engine, reflect=True)

# Save our references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create a session link from Python to the database
session = Session(engine)

# create/define a new Flask app instance
app = Flask(__name__)

# create flask routes
@app.route('/')
# Welcome route
def welcome():
    return(
    f"Welcome to the Climate Analysis API!<br/>"
    f"Available Routes:<br/>"
    f"/api/v1.0/precipitation<br/>"
    f"/api/v1.0/stations<br/>"
    f"/api/v1.0/tobs<br/>"
    f"/api/v1.0/temp/start/end<br/>")

# Precipitation route
@app.route("/api/v1.0/precipitation")
def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)

# Stations Route
@app.route("/api/v1.0/stations")
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)

# Temperature Observations for previous year route
@app.route("/api/v1.0/tobs")
def temp_monthly():
    # date from one year ago
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    # Query the primary station from all temp observations from the previous year
    results = session.query(Measurement.tobs).filter(Measurement.station == "USC00519281").filter(Measurement.date >= prev_year).all()
    # unravel the results into a one-dimensional array and turn it into a list; then jsonify the list and return it
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

# Statistics Route-- need a start and end date, so two different routes
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
# Create a function (no start or end for now)
def stats(start=None, end=None):
    # Create a query to select min, avg, and max temps from SQLite
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
    # create if-not statement to find the start and end date. Query our database using the list^ and then unravel the results
    if not end:
        results = session.query(*sel).filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)
    # calculate the temp min, avg, and max with the start and end dates
    results = session.query(*sel).filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)

