from server import app, engine
from script import relevant
from flask import render_template, request
from sqlalchemy.orm import Session
from model import Fiche



# afficher la fiche 
@app.route('/fiche/<int:id>')
def test(id):
    print(id)
    # with sql conn
    with Session(engine) as session: 
        fiche = session.query(Fiche).get(id)
        
    # sql request 
    # fiche 
    return render_template('fiche.html', fiche=fiche.to_dict())



# mettre a jour la fiche 
@app.route('/updatefiche/<int:id>', methods=['POST'])
def update_fiche(id):
    # with sql conn
    updated_fiche = request.get_json()['fiche']
    with Session(engine) as session: 
        fiche = session.query(Fiche).get(id)
        fiche = Fiche(

        )
        return fiche.to_dict()
    # sql request 
   

# tous les labels 
@app.route('/wihtlabel/<str:label>')
def get_fiche_with_label(label):
    # with sql conn
    with Session(engine) as session: 
        fiches = session.query(Fiche).filter_by(label=label)
        return render_template("bylabel.html", fiches=fiches)
    

 



