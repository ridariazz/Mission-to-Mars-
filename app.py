# we'll use FLask to render a template, redirecting to another url and creating a URL
from flask import Flask, render_template, redirect, url_for
# we're using PyMongo to interact with our mongo database 
from flask_pymongo import PyMongo
# using the scraping code, we'll convert from Jupyter notebook to Python
import scraping
# set up Flask 
app = Flask(__name__)
# tell Python how to connect to Mongo using PyMongo 
# Use flask_pymongo to set up mongo connection
# tells Python that our app will connect to Mongo using a URI (uniform resource identifer) and after = is the URI we'll be using to connect to Mongo
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# define the route for the HTML page 
# tells Flask what to display when we're looking at the home page 
@app.route("/")
def index():
    # find the "mars" collection in our db 
   mars = mongo.db.mars.find_one()
   # tells Flask to return an HTML template using an index.html file 
   return render_template("index.html", mars=mars)

# set up the scraping route
# defines the route that Flask will be using 
@app.route("/scrape")
# allows us to access the database
def scrape():
    # assign new variable that points to our Mongo db
   mars = mongo.db.mars
   # create new variable to hold the newly scraped data ("scrape all" fxn in the scraping.py file exported from Jupyter Notebook)
   mars_data = scraping.scrape_all()
   mars.update_one({}, {"$set":mars_data}, upsert=True)
   return redirect('/', code=302)
# nned for Flask is to tell it to run
if __name__ == "__main__":
   app.run()
