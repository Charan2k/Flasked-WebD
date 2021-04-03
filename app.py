from flask import Flask
from flask import render_template
app = Flask("myapp")

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/table")
def table():
	return render_template("table.html")

@app.route("/youtube")
def youtube():
	return render_template("youtube.html")

@app.route("/wikipedia")
def wikipedia():
	return render_template("wikipedia.html")

@app.route("/form")
def form():
	return render_template("form.html")
