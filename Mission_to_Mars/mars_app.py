# Import dependencies
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# Use flask_pymongo to set up Mongo connection
app.config['MONGO_URI']= 'mongo://localhost:27017/mars_app"
mongo = PyMongo(app)

# Route to main page
@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)

# Create route to Mars scraper
@app.route('/scrape')
def scraper():
    mars= mongo.db.mars
    mars_data = scrape_mars.scrape()
    mars.update({}. mars_data, upsert=True)
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)

