from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.python_files.Database_postgreSQL import OGAGNAGEDB_POSTGRESQL
import os

import psycopg2

app = Flask(__name__)

db = SQLAlchemy(app)

app.config["UPLOAD_FOLDER"] = "C:/Users/Asus/Documents/Formations/Python/ogagnage/app/static/img/"
app.config["SECRET_KEY"] = "Perlembourg49%%%"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/ecnelisflydb.db"
if app.config["ENV"]=='prod' and not KeyError():
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ['DATABASE_URL']
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:Perlembourg49%%%@localhost/ogagnagedb'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

class User_table(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True)
    password = db.Column(db.String(80))


ogagnagedb = OGAGNAGEDB_POSTGRESQL()

from app import views
from app import admin_views

