from flask import Flask
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
res = []
for i in range(no_of_rows):
    res.append(mydata.query.get(i+1)['name'])
    print(res[i]["name"])
