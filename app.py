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
	name = database.Column(database.Text)
	roll = database.Column(database.Text)
	marks = database.Column(database.Text)


	def __init__(self, name, roll, marks):
		self.name = name
		self.roll = roll
		self.marks = marks

database.create_all()


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
	# x = mydata(request.args.get("name"), request.args.get("roll"), request.args.get("marks"))
	# database.session.add(x)
	# database.session.commit()
	no_of_rows = len(mydata.query.all())
	res = [[None]*3]*no_of_rows
	for i in range(no_of_rows):
		j = 0
		res[i][j] = mydata.query.get(i+1).name
		j += 1
		res[i][j] = mydata.query.get(i+1).roll
		j += 1
		res[i][j] = mydata.query.get(i+1).marks
	database.session.commit()
	return render_template("exp.html", no_of_rows = no_of_rows, res=res)