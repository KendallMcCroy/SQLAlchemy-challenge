# Step 1. import Flask
from flask import Flask

# Step 7b. 
from sqlalchemy import create_engine, func, inspect


# Step 2. Create an app, being sure to pass __name__
app = Flask(__name__)

# Stp 7a.
engine = create_engine('sqlite:///Resources/hawaii.sqlite')

# Step 5  Define what to do when a user hits the index route
@app.route("/")
def home():
    print("Server received request for 'Home' page...")
    return "Welcome to my 'Home' page!"


# Step 6 Define what to do when a user hits the /about route
@app.route("/about")
def about():
    print("Server received request for 'About' page...")
    return "Welcome to my 'About' page!"




# Step 3. 
if __name__ == "__main__":
    app.run(debug=True)
