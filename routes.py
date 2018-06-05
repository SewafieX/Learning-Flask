"""When the user types in the URL slash, the function index will run
and return the page index.html"""
#import the flask class and the function render_template
from flask import Flask, render_template 
#creating a new usable instance of the Flask class
app = Flask(__name__)
#map the url "/" int the function index
@app.route("/")
#This python function uses the flask function render_template 
#to render "index.html"
def index():
	return render_template("index.html")

if __name__ == "__main__":
	#app.run runs the app on a local server
	app.run(debug=True) #the flag is to see error messages