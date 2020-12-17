from app import app, ogagnagedb, User_table, db
from flask import request,render_template, redirect,flash
from app.python_files.Moderation import requires_auth
from flask_login import login_user, login_required, logout_user
import boto3
from app.config import S3_BUCKET, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, DATABASE_URL
s3 = boto3.client('s3',
                    aws_access_key_id=AWS_ACCESS_KEY_ID,
                    aws_secret_access_key= AWS_SECRET_ACCESS_KEY,
                     )

@app.route('/admin/form')
@requires_auth
def home_admin():
    return render_template("admin/form.html")

@app.route('/validation', methods=['POST'])
def afficher_form_2():
    reponse = request.form
    ogagnagedb.update_infos(reponse)
    return render_template("admin/form_2.html")

@app.route('/validation_2', methods=['POST', 'GET'])
def home_admin_ajouté():
    file = request.files['image']
    filename = file.filename
    ogagnagedb.update_filepath(filename)
    s3_resource = boto3.resource('s3')
    my_bucket = s3_resource.Bucket(S3_BUCKET)
    my_bucket.Object(filename).put(Body=file, ACL='public-read')
    return render_template("admin/home_ajouté.html")

@app.route('/admin/supp')
@requires_auth
def supp_admin():
    liste_db=ogagnagedb.scan_complet()
    return render_template("admin/supp.html",liste_db=liste_db)

@app.route('/admin/valid_supp',methods=['POST', 'GET'])
@requires_auth
def valid_supp():
    reponse = request.form
    id_carte=reponse['id_carte']
    print(type(id_carte))
    filename_to_delete=ogagnagedb.filename_to_delete(id_carte)
    s3_resource = boto3.resource('s3')
    my_bucket = s3_resource.Bucket(S3_BUCKET)
    my_bucket.Object(filename_to_delete).delete()
    ogagnagedb.delete_carte(id_carte)
    liste_db=ogagnagedb.scan_complet()
    return render_template("admin/supp.html",liste_db=liste_db)




