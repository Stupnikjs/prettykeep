import os 
from flask import Flask

app = Flask(__name__, template_folder="static/templates")

from router import *


port = "5000"

if port == "":
    port = os.environ.get('PORT')

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=port)