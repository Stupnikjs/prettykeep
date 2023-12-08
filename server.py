import os 
from flask import Flask 

app = Flask(__name__)

from router import *

app.run(host="0.0.0.0", port=os.environ['PORT'])