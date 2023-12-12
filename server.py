import os 
from datetime import datetime 
from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from script import relevant
from model import Fiche


app = Flask(__name__, template_folder="static/templates")

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

'''
A metre dans une init db 
for fiche in relevant:
    fiche['created'] = today
    fiche['updated'] = None 
    print(fiche)
    with Session(engine) as session:
        fiche['created'] = today
        fiche['updated'] = None
        newfiche=Fiche(
            title=fiche['title'],
            text=fiche['text'],
            created=fiche['created'],
            updated=fiche['updated'],
            labels=fiche['labels']
            )
        session.add(newfiche)
        session.commit()
'''

    
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=port)