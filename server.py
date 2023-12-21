import os 
from datetime import datetime

from sqlalchemy import create_engine 
from app import create_app
from flask import Flask
from config import DevelopmentConfig
from router import create_routes

app = Flask(__name__)





"""
if 'DB_URI' in os.environ: 
    uri=os.environ['DB_URI']
else: 
    uri = "postgresql://vxxssqap:nX4LrcOIo9uQ1OQtPpXHm6PEm5MC_lDx@horton.db.elephantsql.com/vxxssqap"
"""



app = create_app(DevelopmentConfig)


engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])

create_routes(app, engine)

today = datetime.now().strftime("%d-%m-%Y %H:%M")

# middleware authentification
 
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=app.config['PORT'])