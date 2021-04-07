from re import S
from flask import Flask
from flask import render_template
from flask import Request
from flask.globals import request 
from flask_sqlalchemy import SQLAlchemy

app = Flask("myapp")
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///static/database/mydata.sqlite"

database = SQLAlchemy(app)
class mydata(database.Model):
	id = database.Column(database.Integer, primary_key = True)
	name = database.Column(database.String(30))
	roll = database.Column(database.Integer)
	marks = database.Column(database.Integer)


	def __init__(self, name, roll, marks):
		self.name = name
		self.roll = roll
		self.marks = marks


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

@app.route("/updated",methods=['GET'])
def updated():
	for i in range(10):
		x = mydata(request.args.get("name"), request.args.get("roll"), request.args.get("marks"))
		database.session.add(x)
	database.session.commit()
	# return render_template("exp.html", name=x.name, roll=x.roll, marks=x.marks)
	return render_template("updated.html")

@app.route("/update")
def update():
    	return render_template("update.html")

@app.route('/get_details')
def get_details():		
	rows = mydata.query.all()
	return render_template("exp.html", rows=rows)


if __name__ == '__main__':
	app.run(debug=True)