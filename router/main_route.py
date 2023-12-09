from server import app 
from script import relevant
from flask import render_template


@app.route('/')
def index():
    return 'Hello'


@app.route('/test')
def test():
    return render_template('fiche.html', data=relevant)

