class config:
    DEBUG = True
    TESTING = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:liliana@localhost:3306/taller'


class ProductionConfig(config):
    DEBUG = False
    TESTING = False
    
    class DevelopmentConfig(config):
        SECRET_KEY = 'dev'
        DEBUG = True
        TESTING = True