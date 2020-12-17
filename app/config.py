import os

S3_LOCATION = 'http://your-amazon-site.amazonaws.com/'
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
S3_BUCKET = "ogagnage"
DATABASE_URL = os.environ.get("DATABASE_URL")
DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD")
SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
SQLALCHEMY_BINDS=os.environ.get("SQLALCHEMY_BINDS")