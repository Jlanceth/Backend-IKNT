import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
  SECRET_KEY = os.environ.get('SECRET_KEY') or '123321admin'

  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'PostgreSQL:///' + os.path.join(basedir, 'app.db')

  SQLALCHEMY_TRACK_MODIFICATIONS = False