class Config(object):
    DEBUG = True
    SECRET_HERE = '249y823r9v8238r9u'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///./movies.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_JSON_AS_ASCII = False
    JSON_SORT_KEYS = False
    PORT = 10001
