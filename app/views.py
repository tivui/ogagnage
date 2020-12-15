from app import app, ogagnagedb, User_table,db
from flask import request,render_template, redirect,flash
from flask_login import login_user, login_required, logout_user

@app.route('/')
def afficher_home():
    return render_template("/public/home.html")

@app.route('/oiseaux')
def oiseaux():
    env=app.config['ENV']
    DATABASE_URL = app.config["SQLALCHEMY_DATABASE_URI"]
    type='oiseau'
    liste_db=ogagnagedb.scan_type(type,env,DATABASE_URL)
    titre='Oiseaux du Gagnage'
    return render_template("/public/cards.html",liste_db=liste_db,titre=titre)

@app.route('/mammiferes')
def mammiferes():
    env=app.config['ENV']
    DATABASE_URL = app.config["SQLALCHEMY_DATABASE_URI"]
    type='mammifere'
    liste_db=ogagnagedb.scan_type(type,env,DATABASE_URL)
    titre='Mammifères du Gagnage'
    return render_template("/public/cards.html",liste_db=liste_db,titre=titre)

@app.route('/fleurs')
def fleurs():
    env=app.config['ENV']
    DATABASE_URL = app.config["SQLALCHEMY_DATABASE_URI"]
    type='fleur'
    liste_db=ogagnagedb.scan_type(type,env,DATABASE_URL)
    titre='Fleurs du Gagnage'
    return render_template("/public/cards.html",liste_db=liste_db,titre=titre)

@app.route('/arbres')
def arbres():
    env=app.config['ENV']
    DATABASE_URL = app.config["SQLALCHEMY_DATABASE_URI"]
    type='arbre'
    liste_db=ogagnagedb.scan_type(type,env,DATABASE_URL)
    titre='Arbres du Gagnage'
    return render_template("/public/cards.html",liste_db=liste_db,titre=titre)

@app.route('/arbustes')
def arbustes():
    env=app.config['ENV']
    DATABASE_URL = app.config["SQLALCHEMY_DATABASE_URI"]
    type='arbuste'
    liste_db=ogagnagedb.scan_type(type,env,DATABASE_URL)
    titre='Arbustes du Gagnage'
    return render_template("/public/cards.html",liste_db=liste_db,titre=titre)


