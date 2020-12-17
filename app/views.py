from app import app, ogagnagedb, User_table,db
from flask import request,render_template, redirect,flash
from flask_login import login_user, login_required, logout_user
from app.config import DATABASE_URL

@app.route('/')
def afficher_home():
    print(app.config["ENV"])
    return render_template("/public/home.html")

@app.route('/oiseaux')
def oiseaux():
    print(DATABASE_URL)
    type='oiseau'
    liste_db=ogagnagedb.scan_type(type)
    titre='Oiseaux du Gagnage'
    return render_template("/public/cards.html",liste_db=liste_db,titre=titre)

@app.route('/mammiferes')
def mammiferes():
    env=app.config['ENV']
    type='mammifere'
    liste_db=ogagnagedb.scan_type(type)
    titre='Mammifères du Gagnage'
    return render_template("/public/cards.html",liste_db=liste_db,titre=titre)

@app.route('/fleurs')
def fleurs():
    env=app.config['ENV']
    type='fleur'
    liste_db=ogagnagedb.scan_type(type)
    titre='Fleurs du Gagnage'
    return render_template("/public/cards.html",liste_db=liste_db,titre=titre)

@app.route('/arbres')
def arbres():
    env=app.config['ENV']
    type='arbre'
    liste_db=ogagnagedb.scan_type(type)
    titre='Arbres du Gagnage'
    return render_template("/public/cards.html",liste_db=liste_db,titre=titre)

@app.route('/arbustes')
def arbustes():
    env=app.config['ENV']
    type='arbuste'
    liste_db=ogagnagedb.scan_type(type)
    titre='Arbustes du Gagnage'
    return render_template("/public/cards.html",liste_db=liste_db,titre=titre)


