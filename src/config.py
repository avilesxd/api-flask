# A class that is used to configure the Flask application.
class DevelopmentConfig():
    DEBUG = True


# A dictionary that maps the string 'development' to the class DevelopmentConfig.
config = {
    'development': DevelopmentConfig
}
