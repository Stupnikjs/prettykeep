from server import app, engine
from script import relevant
from flask import render_template, request
from sqlalchemy.orm import Session
from model import Fiche

def get_labels(dict):
    # loop over labels and check prop "name" and return a list of boolean, if one is true any() return true
    return dict['labels'][0]['name']

'''
def has_labels(x, dict):
    return x == get_labels(dict)

all_labels = map(get_labels,relevant)

@app.route('/')
def index():
    return 'Hello'

'''



@app.route('/fiche/<int:id>')
def test(id):
    print(id)
    # with sql conn
    with Session(engine) as session: 
        fiche = session.query(Fiche).get(id)
        
    # sql request 
    # fiche 
    return render_template('fiche.html', fiche=fiche.to_dict())


@app.route('/updatefiche/<int:id>', methods=['POST'])
def update_fiche(id):
    # with sql conn
    with Session(engine) as session: 
        fiche = session.query(Fiche).get(id)
    # sql request 
    # fiche 
    try: 

    except:
        
    return 


@app.route('/sortby/', methods=['POST'])
def sortby():
    param = request.get_json()
    print(param)
    print(relevant[0])
    return get_labels(relevant[0])
    '''
       if param['search'] not in all_labels:
        return 'error'
    else: 
        sorted = filter( lambda x: has_labels(x, relevant), relevant)
    return sorted
    '''
 

