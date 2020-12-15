import psycopg2
import boto3
from app.config import S3_BUCKET, S3_KEY, S3_SECRET
from app.config import DATABASE_URL
s3 = boto3.client('s3',
                    aws_access_key_id=S3_KEY,
                    aws_secret_access_key= S3_SECRET,
                     )


class OGAGNAGEDB_POSTGRESQL():

    def update_infos(self, reponse,env,DATABASE_URL):
        if env == 'dev':
            connection = psycopg2.connect(user="postgres",
                                      password="Perlembourg49%%%",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="ogagnagedb")
        elif env == 'prod':
            connection = psycopg2.connect(DATABASE_URL, sslmode='require')
        cursor = connection.cursor()
        if reponse['type']=='oiseau':
            new_infos = (reponse['type'], reponse['name'], reponse['taille'],reponse['nourriture'],reponse['infos'])
            cursor.execute(
                "INSERT INTO infodb (type,name,taille,nourriture,infos) VALUES(%s,%s,%s,%s,%s)",
                new_infos)
        elif reponse['type']=='mammifere':
            new_infos = (reponse['type'], reponse['name'], reponse['taille'],reponse['nourriture'],reponse['infos'])
            cursor.execute(
                "INSERT INTO infodb (type,name,taille,nourriture,infos) VALUES(%s,%s,%s,%s,%s)",
                new_infos)
        elif reponse['type']=='fleurs':
            new_infos = (reponse['type'], reponse['name'], reponse['exposition'],reponse['floraison'],reponse['infos'])
            cursor.execute(
                "INSERT INTO infodb (type,name,exposition,floraison,infos) VALUES(%s,%s,%s,%s,%s)",
                new_infos)
        elif reponse['type']=='arbre':
            new_infos = (reponse['type'], reponse['name'], reponse['feuillage'],reponse['nb'],reponse['fruit'],reponse['infos'])
            cursor.execute(
                "INSERT INTO infodb (type,name,feuillage,nb,fruit,infos) VALUES(%s,%s,%s,%s,%s,%s)",
                new_infos)
        elif reponse['type']=='arbute':
            new_infos = (reponse['type'], reponse['name'], reponse['feuillage'],reponse['nb'],reponse['infos'])
            cursor.execute(
                "INSERT INTO infodb (type,name,feuillage,nb,infos) VALUES(%s,%s,%s,%s,%s)",
                new_infos)
        connection.commit()
        connection.close()

    def update_filepath (self,filename,env,DATABASE_URL):
        if env == 'dev':
            connection = psycopg2.connect(user="postgres",
                                      password="Perlembourg49%%%",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="ogagnagedb")
        elif env == 'prod':
            connection = psycopg2.connect(DATABASE_URL, sslmode='require')
        cursor = connection.cursor()
        cursor.execute( "SELECT MAX(Id) FROM infodb" )
        ligne_max = str(cursor.fetchone()[0])
        cursor.execute(
            "UPDATE infodb SET image = %s WHERE id=" + ligne_max,
            (filename,))
        connection.commit()
        connection.close()

    def scan_type(self,type,envi,DATABASE_URL):
        if envi == 'dev':
            connection = psycopg2.connect(user="postgres",
                                          password="Perlembourg49%%%",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="ogagnagedb")
        elif envi == 'prod':
            connection = psycopg2.connect(DATABASE_URL, sslmode='require')
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM infodb WHERE type=%s",(type,))
        return cursor.fetchall()

    def scan_complet(self,env,DATABASE_URL):
        if env == 'dev':
            connection = psycopg2.connect(user="postgres",
                                          password="Perlembourg49%%%",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="ogagnagedb")
        elif env == 'prod':
            connection = psycopg2.connect(DATABASE_URL, sslmode='require')
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM infodb")
        return cursor.fetchall()

    def delete_carte(self,id_carte,env,DATABASE_URL):
        if env == 'dev':
            connection = psycopg2.connect(user="postgres",
                                      password="Perlembourg49%%%",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="ogagnagedb")
        cursor = connection.cursor()
        cursor.execute("DELETE FROM infodb WHERE id=" + id_carte)
        connection.commit()
        connection.close()

    def filename_to_delete(self,id_carte,env,DATABASE_URL):
        if env == 'dev':
            connection = psycopg2.connect(user="postgres",
                                          password="Perlembourg49%%%",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="ogagnagedb")
        elif env == 'prod':
            connection = psycopg2.connect(DATABASE_URL, sslmode='require')
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM infodb WHERE id=" + id_carte)
        return cursor.fetchone()[3]

