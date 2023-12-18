import os 
from datetime import datetime 
from app import create_app
from sqlalchemy import create_engine

# from script import relevant



app = create_app()

from router import *
from orm import Base 



port = os.environ.get('PORT')

if port == "":
    port = "5000"



if 'DB_URI' in os.environ: 
    uri=os.environ['DB_URI']
else: 
    uri='postgresql://mavkwomw:AcfRavZm6hKU42I0rDRzYcruMuFtI8D6@horton.db.elephantsql.com/mavkwomw'



engine = create_engine(uri, pool_size=4, max_overflow=2)

Base.metadata.create_all(engine, checkfirst=True)

today = datetime.now().strftime("%d-%m-%Y %H:%M")

# middleware authentification
 
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=port)