

# Step 1. import Flask
from flask import Flask, jsonify

# Step 7b. 
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

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
        f"Welcome to Surf's Up Climate App API!<br>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
    )


# Step 6 Define what to do when a user hits the /about route
@app.route("/about")
def about():
    print("Server received request for 'About' page...")
    return "Welcome to my 'About' page!"




# Step 3. 
if __name__ == "__main__":
    app.run(debug=True)
