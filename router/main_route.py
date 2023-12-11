from server import app 
from script import relevant
from flask import render_template, request

def get_labels(dict):
    return dict['labels']['name']

allLabels = map(get_labels,relevant)



@app.route('/')
def index():
    return 'Hello'


@app.route('/test')
def test():
    return render_template('fiche.html', data=relevant)

@app.route('/sortby/', methods=['POST'])
def sortby():
    param = request.get_json()
    
    if param['search'] not in relevant
    filter()
    return 

