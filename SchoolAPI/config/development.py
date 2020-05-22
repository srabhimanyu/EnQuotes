import os

basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, '../data-dev.sqlite')

DEBUG = True
IGNORE_AUTH = True
SECRET_KEY = 'top-secret!'
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://abhi:abhi@localhost:3306/dbname'
SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
SSL_DISABLE = False
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
SQLALCHEMY_RECORD_QUERIES = True
MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
FLASKY_MAIL_SUBJECT_PREFIX = '[SchoolApp]'
FLASKY_MAIL_SENDER = 'Sumit Bansal <sumit.asr@gmail.com>'
FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')