

# Step 1. import Flask
from flask import Flask, jsonify

# Step 7b. 
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import numpy as np

# Step 2. Create an app, being sure to pass __name__
app = Flask(__name__)

# Step 7a.
engine = create_engine('sqlite:///Resources/hawaii.sqlite')


#########################
# Step 8 Set up data base
#########################
 # reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the tables
Measurement = Base.classes.measurement
Station = Base.classes.station


############################################################################################
# Step 5 FLASK Routes 1st INDEX ROUTE... Define what to do when a user hits the index route
############################################################################################
@app.route("/")
def home():
    print("Server received request for 'Home' page...")
    return (
        f"Home<br>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
    )
##########################################################
#PRECIPITATION Data
##########################################################
@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

       # Query all precipitation
    results = session.query(Measurement.date, Measurement.prcp, Measurement.station).all()
    
    session.close()

    all_precipitation = []
    # for date, in Measurement:
    for result in results:
        # if prcp  != None:
            precip_dict = {}
            precip_dict = {result.date: result.prcp, "Station": result.station}
            # precip_dict["date"] = date
            all_precipitation.append(precip_dict)
           
     # Convert list of tuples into normal list
    # all_precipitation = list(np.ravel(results))
    return jsonify(all_precipitation)

################################################
#Station
################################################
@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    #Query for stations
    stations = session.query(Station.station, Station.name, Station.latitude, Station.longitude, Station.elevation).all()

    session.close()

# Create a dictionary to convert the query results
    all_stations = []
    for station, name, latitude, longitude, elevation in stations:
        station_dict = {}
        station_dict["station"] = station
        station_dict["name"] = name
        station_dict["latitude"] = latitude
        station_dict["longitude"] = longitude
        station_dict["elevation"] = elevation
        all_stations.append(station_dict)

        return jsonify(all_stations)

# Step 6 Define what to do when a user hits the /about route
@app.route("/about")
def about():
    print("Server received request for 'About' page...")
    return "Welcome to my 'About' page!"




# Step 3. 
if __name__ == "__main__":
    app.run(debug=True)
