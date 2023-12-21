import base64
from flask import Flask
from sqlalchemy import create_engine
from urllib.parse import quote
from config import Config


def create_app(config_class=Config):

    app = Flask(__name__, template_folder="static/templates")
    
    
    def custom_urlsafe_b64encode(value):
        encoded_value = base64.urlsafe_b64encode(value.encode('utf-8')).decode('utf-8')
        return quote(encoded_value, safe='')

    app.jinja_env.filters['urlsafe_b64encode'] = custom_urlsafe_b64encode
    app.config.from_object(config_class)
    

    return app