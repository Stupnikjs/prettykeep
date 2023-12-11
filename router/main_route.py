from server import app 
from script import relevant
from flask import render_template, request

def get_labels(dict):
    return dict['labels'][0]['name']

'''
def has_labels(x, dict):
    return x == get_labels(dict)

all_labels = map(get_labels,relevant)
'''




@app.route('/')
def index():
    return 'Hello'


@app.route('/test')
def test():
    return render_template('fiche.html', data=relevant)

@app.route('/sortby/', methods=['POST'])
def sortby():
    param = request.get_json()
    print(param)
    print(relevant[0])
    return relevant[0]
    '''
       if param['search'] not in all_labels:
        return 'error'
    else: 
        sorted = filter( lambda x: has_labels(x, relevant), relevant)
    return sorted
    '''
 

