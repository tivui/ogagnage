from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.python_files.Database_postgreSQL import OGAGNAGEDB_POSTGRESQL
import os

import psycopg2

app = Flask(__name__)

db = SQLAlchemy(app)

app.config["UPLOAD_FOLDER"] = "C:/Users/Asus/Documents/Formations/Python/ogagnage/app/static/img/"
app.config["SECRET_KEY"] = "Perlembourg49%%%"
if app.config["ENV"]=='prod':
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://yfbpfzchmeimka:c2a276287cf7cab71b0d92600f28f2104d449a3fd061d50a6f73f41830250820@ec2-54-217-204-34.eu-west-1.compute.amazonaws.com:5432/dnuo27dukd0qh"
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:Perlembourg49%%%@localhost/ogagnagedb'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

class User_table(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True)
    password = db.Column(db.String(80))


ogagnagedb = OGAGNAGEDB_POSTGRESQL()

from app import views
from app import admin_views

