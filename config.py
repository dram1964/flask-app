import os
from dotenv import load_dotenv

load_dotenv()

class Config():
    SECRET_KEY  = os.environ.get('SECRET_KEY') or 'the-default-development-value'
    SQLALCHEMY_DATABASE_URI = os.environ.get('PSQL_CONNECTION_STRING') or 'postgresql://scott:tiger@localhost/mydatabase'
