import os 
from flask import Flask
from sqlalchemy import create_engine

app = Flask(__name__, template_folder="static/templates")

from router import *


port = "5000"

if port == "":
    port = os.environ.get('PORT')

uri = ''

if 'DB_URI' in os.environ: 
    uri=os.environ['DB_URI']

engine = create_engine(uri)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=port)