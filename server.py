import os 
from datetime import datetime

from sqlalchemy import create_engine 
from app import create_app
from flask import Flask
from config import DevelopmentConfig
from router import create_routes

app = Flask(__name__)


app = create_app(DevelopmentConfig)


engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])

create_routes(app, engine)

today = datetime.now().strftime("%d-%m-%Y %H:%M")

# middleware authentification
 
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=app.config['PORT'])