import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

file_path = os.path.abspath(os.getcwd())+'/database/FOSSchan2.db'

"""This needs to be isolated to support blueprints and models"""
app = Flask(__name__)
dbURI = 'sqlite:///'+file_path

# Setup properties for the database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = dbURI
app.config['SECRET_KEY'] = 'SECRET_KEY'
db = SQLAlchemy(app)
Migrate(app, db)
print("!")
print(dbURI)