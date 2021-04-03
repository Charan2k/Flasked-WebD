from flask import Flask
from flask import render_template
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

@app.route("/db",methods=['GET'])
def db():
	x = mydata("charan","1","56")
	database.session.add(x)
	database.session.commit()
	return "Domne"

@app.route('/get_details')
def get_details():
	r1 = mydata.query.get(1)
	return render_template("exp.html", name=str(r1.name), roll=str(r1.roll), marks=str(r1.marks))
