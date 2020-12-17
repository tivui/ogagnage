import psycopg2
import boto3
from app.config import DATABASE_URL,AWS_ACCESS_KEY_ID,AWS_SECRET_ACCESS_KEY,DATABASE_PASSWORD
s3 = boto3.client('s3',
                    aws_access_key_id=AWS_ACCESS_KEY_ID,
                    aws_secret_access_key= AWS_SECRET_ACCESS_KEY,
                     )
from flask import current_app


class OGAGNAGEDB_POSTGRESQL():

    def update_infos(self, reponse):
        connection = psycopg2.connect(user="fyuujerfzmpxgf",
                                          password="76e9998da230d3998b8cb4f145fbe10d326c77f252b47e5fbabb188f8aeb0f9e",
                                          host="ec2-54-75-246-118.eu-west-1.compute.amazonaws.com",
                                          port="5432",
                                          database="dchmdui7vcgm07")
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
        elif reponse['type']=='fleur':
            new_infos = (reponse['type'], reponse['name'], reponse['exposition'],reponse['floraison'],reponse['infos'])
            cursor.execute(
                "INSERT INTO infodb (type,name,exposition,floraison,infos) VALUES(%s,%s,%s,%s,%s)",
                new_infos)
        elif reponse['type']=='arbre':
            new_infos = (reponse['type'], reponse['name'], reponse['feuillage'],reponse['nb'],reponse['fruit'],reponse['infos'])
            cursor.execute(
                "INSERT INTO infodb (type,name,feuillage,nb,fruit,infos) VALUES(%s,%s,%s,%s,%s,%s)",
                new_infos)
        elif reponse['type']=='arbuste':
            new_infos = (reponse['type'], reponse['name'], reponse['feuillage'],reponse['nb'],reponse['infos'])
            cursor.execute(
                "INSERT INTO infodb (type,name,feuillage,nb,infos) VALUES(%s,%s,%s,%s,%s)",
                new_infos)
        connection.commit()
        connection.close()

    def update_filepath (self,filename):
        connection = psycopg2.connect(user="fyuujerfzmpxgf",
                                          password=DATABASE_PASSWORD,
                                          host="ec2-54-75-246-118.eu-west-1.compute.amazonaws.com",
                                          port="5432",
                                          database="dchmdui7vcgm07")
        cursor = connection.cursor()
        cursor.execute( "SELECT MAX(Id) FROM infodb" )
        ligne_max = str(cursor.fetchone()[0])
        cursor.execute(
            "UPDATE infodb SET image = %s WHERE id=" + ligne_max,
            (filename,))
        connection.commit()
        connection.close()

    def scan_type(self,type):
        connection = psycopg2.connect(user="fyuujerfzmpxgf",
                                          password=DATABASE_PASSWORD,
                                          host="ec2-54-75-246-118.eu-west-1.compute.amazonaws.com",
                                          port="5432",
                                          database="dchmdui7vcgm07")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM infodb WHERE type=%s ORDER BY name ASC",(type,))
        return cursor.fetchall()

    def scan_complet(self):
        if (current_app.config["ENV"]=='prod') or (current_app.config["ENV"]=='production'):
            connection = psycopg2.connect(user="fyuujerfzmpxgf",
                                              password=DATABASE_PASSWORD,
                                              host="ec2-54-75-246-118.eu-west-1.compute.amazonaws.com",
                                              port="5432",
                                              database="dchmdui7vcgm07")
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM infodb ORDER BY name ASC")
            return cursor.fetchall()


    def delete_carte(self,id_carte,env,DATABASE_URL):
        connection = psycopg2.connect(user="fyuujerfzmpxgf",
                                          password="76e9998da230d3998b8cb4f145fbe10d326c77f252b47e5fbabb188f8aeb0f9e",
                                          host="ec2-54-75-246-118.eu-west-1.compute.amazonaws.com",
                                          port="5432",
                                          database="dchmdui7vcgm07")
        cursor = connection.cursor()
        cursor.execute("DELETE FROM infodb WHERE id=" + id_carte)
        connection.commit()
        connection.close()

    def filename_to_delete(self,id_carte,env,DATABASE_URL):
        connection = psycopg2.connect(user="fyuujerfzmpxgf",
                                          password="76e9998da230d3998b8cb4f145fbe10d326c77f252b47e5fbabb188f8aeb0f9e",
                                          host="ec2-54-75-246-118.eu-west-1.compute.amazonaws.com",
                                          port="5432",
                                          database="dchmdui7vcgm07")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM infodb WHERE id=" + id_carte)
        return cursor.fetchone()[3]

