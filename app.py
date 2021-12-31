

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
        f"/api/v1.0/start<br/>"
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
            precip_dict = {}
            precip_dict = {result.date: result.prcp, "Station": result.station}
            all_precipitation.append(precip_dict)
           
     # Convert list of tuples into normal list
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

###############################################
# Tobs 
###############################################

###############################################
# Start Date list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range
###############################################


@app.route("/api/v1.0/start")
def start_date():

    # Create our session (link) from Python to the DB
    session = Session(engine)
    #
    sel = [Measurement.date, func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    results = (session.query(*sel))
                   
    session.close()

    start_date = []
    for result in results:
        date_dict = {}
        date_dict["Date"] = result[0]
        date_dict["Low Temp"] = result[1]
        date_dict["Avg Temp"] = result[2]
        date_dict["High Temp"] = result[3]
        start_date.append(date_dict)
        
        return jsonify(start_date)


###############################################
# Start/End Date
# ###############################################
# @app.route("/api/v1.0/start/end")
# def ():
#     # Create our session (link) from Python to the DB
#     session = Session(engine)

#        # Query all 
#     results = session.query(Measurement.date, Measurement.prcp, Measurement.station).all()
    
#     session.close()




# Step 3. 
if __name__ == "__main__":
    app.run(debug=True)
