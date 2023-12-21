import os

class Config:
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = ''
    
    # Other configuration options

class DevelopmentConfig(Config):
    DEBUG = True
    PORT = os.environ.get('PORT', '5000')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DB_URI', "postgresql://vxxssqap:nX4LrcOIo9uQ1OQtPpXHm6PEm5MC_lDx@horton.db.elephantsql.com/vxxssqap")
class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://lziqbjkd:HP_7F8AFjzdQO8vXtVPrEJLV0wRRcML2@dumbo.db.elephantsql.com:5432/lziqbjkd'
    PORT = '4000'
    # Other configuration options for testing