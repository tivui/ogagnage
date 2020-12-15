from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.python_files.Database_postgreSQL import OGAGNAGEDB_POSTGRESQL
import os
from app.config import SQLALCHEMY_DATABASE_URI

import psycopg2

app = Flask(__name__)

db = SQLAlchemy(app)
app.config["UPLOAD_FOLDER"] = "C:/Users/Asus/Documents/Formations/Python/ogagnage/app/static/img/"
app.config["SECRET_KEY"] = "Perlembourg49%%%"
if app.config["ENV"]=='prod':
    app.config["DATABASE_URL"] = "postgres://fyuujerfzmpxgf:76e9998da230d3998b8cb4f145fbe10d326c77f252b47e5fbabb188f8aeb0f9e@ec2-54-75-246-118.eu-west-1.compute.amazonaws.com:5432/dchmdui7vcgm07"
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://fyuujerfzmpxgf:76e9998da230d3998b8cb4f145fbe10d326c77f252b47e5fbabb188f8aeb0f9e@ec2-54-75-246-118.eu-west-1.compute.amazonaws.com:5432/dchmdui7vcgm07"
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

