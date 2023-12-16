from server import app, engine
from flask import render_template, request
from sqlalchemy.orm import Session
from model import Fiche



# afficher la fiche 
@app.route('/fiche/<int:id>')
def test(id):
    # with sql conn
    with Session(engine) as session: 
        fiche = session.query(Fiche).get(id)
    return render_template('fiche.html', fiche=fiche)



# mettre a jour la fiche 
@app.route('/updatefiche/<int:id>', methods=['POST'])
def update_fiche(id):
    # with sql conn
    updated_fiche = request.get_json()['fiche']
    # gérer erreur dans le json 
    
    with Session(engine) as session: 
        fiche = session.query(Fiche).get(id)
        fiche = Fiche(
         title=updated_fiche['title'],
         text=updated_fiche['text'],
         labels=updated_fiche['labels'],
         created=updated_fiche['created'],
         updated=updated_fiche['updated'], 
         complete_start=updated_fiche['complete_start'],
         complete_end=updated_fiche['complete_end']
        )
        return fiche.to_dict()
    # sql request 
   

# tous les labels 
@app.route('/withlabel/<string:label>')
def get_fiche_with_label(label):
    # with sql conn
    with Session(engine) as session: 
        fiches = session.query(Fiche).filter_by(labels=label)
        return_fiches = []
        for fiche in fiches:
            
            return_fiches.append(fiche.to_dict())
        print(return_fiches)
        return render_template("bylabel.html", fiches=return_fiches)
    

 

# supprimer la fiche 
@app.route('/deletefiche/<int:id>')
def delete_fiche(id):
    # with sql conn
    with Session(engine) as session: 
        fiche = session.query(Fiche).get(id)
        session.delete(fiche)
        session.commit()
    # sql request 
    # fiche 
    return render_template('fiche.html', fiche=fiche.to_dict())


