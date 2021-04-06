import re
from flask import Flask
from flask.templating import render_template_string
from flask_sqlalchemy import SQLAlchemy
app = Flask("test")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.sqlite"
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

no_of_rows = len(mydata.query.all())
res = [[None]*3]*no_of_rows

for i in range(no_of_rows):
	j = 0
	res[i][j] = mydata.query.get(i+1).name
	j += 1
	res[i][j] = mydata.query.get(i+1).roll
	j += 1
	res[i][j] = mydata.query.get(i+1).marks
print(res)




# testting 
no_of_rows = len(mydata.query.all())
res = [{"name": None,
		"roll": None,
		"marks": None}]*no_of_rows
for i in range(no_of_rows):
	res[i]["name"] = mydata.query.get(i+1).name
	res[i]["roll"] = mydata.query.get(i+1).roll
	res[i]["marks"] = mydata.query.get(i+1).marks