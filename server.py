import os 
from datetime import datetime 
from app import create_app
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
# from script import relevant



app = create_app()

from router import *
from model import Base 

port = "5000"

if port == "":
    port = os.environ.get('PORT')

uri = ''

if 'DB_URI' in os.environ: 
    uri=os.environ['DB_URI']

uri= "postgresql://qedivgso:GlAGhCxeJjsTKv_MoVz35OAjyxCXTeS9@tyke.db.elephantsql.com/qedivgso" 

engine = create_engine(uri)

Base.metadata.create_all(engine, checkfirst=True)
# Base.metadata.drop_all(engine)
today = datetime.now().strftime("%d-%m-%Y %H:%M")

# middleware authentification


    
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=port)