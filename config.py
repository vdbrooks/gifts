import os

basedir = os.path.abspath(os.path.dirname(__file__))

#Enable XSS Protection
WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

#Configure DB URI and migration files folder
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
