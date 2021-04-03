from flask import Flask
from flask import render_template
app = Flask("myapp")

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/table")
def table():
	return render_template("table.html")
