from app import app, ogagnagedb, User_table,db
from flask import request,render_template, redirect,flash
from flask_login import login_user, login_required, logout_user
from app.config import DATABASE_URL

@app.route('/sw.js')
def sw():
    return app.send_from_directory('static','sw.js')

@app.route('/manifest.json')
def manifest():
    return app.send_from_directory('static', 'manifest.json')

@app.route('/')
def afficher_home():
    return render_template("/public/home.html")

@app.route('/oiseaux')
def oiseaux():
    type='oiseau'
    liste_db=ogagnagedb.scan_type(type)
    titre='Oiseaux du Gagnage'
    return render_template("/public/cards.html",liste_db=liste_db,titre=titre)

@app.route('/mammiferes')
def mammiferes():
    type='mammifere'
    liste_db=ogagnagedb.scan_type(type)
    titre='Mammifères du Gagnage'
    return render_template("/public/cards.html",liste_db=liste_db,titre=titre)

@app.route('/fleurs')
def fleurs():
    type='fleur'
    liste_db=ogagnagedb.scan_type(type)
    titre='Fleurs du Gagnage'
    return render_template("/public/cards.html",liste_db=liste_db,titre=titre)

@app.route('/arbres')
def arbres():
    type='arbre'
    liste_db=ogagnagedb.scan_type(type)
    titre='Arbres du Gagnage'
    return render_template("/public/cards.html",liste_db=liste_db,titre=titre)

@app.route('/arbustes')
def arbustes():
    type='arbuste'
    liste_db=ogagnagedb.scan_type(type)
    titre='Arbustes du Gagnage'
    return render_template("/public/cards.html",liste_db=liste_db,titre=titre)


