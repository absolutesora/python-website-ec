import os

datadir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # this is for FLASK password to generate token. CSRF protection
    SECRET_KEY = os.environ.get('SECRET_PASS') or 'PasswordFlask'
    # this config is for SQlite database environment values
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(datadir,'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SMTP config values
    MAIL_DOMAIN = os.environ.get('MAIL_DOMAIN')
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['taka@austlink.com.au']
    # Pagination
    POST_PER_PAGE = 25
    # Language support using Babel
    LANGUAGES = ['en', 'ja']