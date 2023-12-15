from server import app, engine
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
    # gérer erreur dans le json 
    
    with Session(engine) as session: 
        fiche = session.query(Fiche).get(id)
        fiche = Fiche(
         title=updated_fiche['title'],
         text=updated_fiche['text'],
         labels=updated_fiche['labels'],
         created=updated_fiche['created']
         updated=updated_fiche['updated'], 
         #complete=updated_fiche['complete']
        )
        return fiche.to_dict()
    # sql request 
   

# tous les labels 
@app.route('/wihtlabel/<string:label>')
def get_fiche_with_label(label):
    # with sql conn
    with Session(engine) as session: 
        fiches = session.query(Fiche).filter_by(label=label)
        return render_template("bylabel.html", fiches=fiches)
    

 

# supprimer la fiche 
@app.route('/delete_fiche/<int:id>')
def delete_fiche(id):
    # with sql conn
    with Session(engine) as session: 
        # fiche = session.query(Fiche).get(id) delete 
        
    # sql request 
    # fiche 
    return render_template('fiche.html', fiche=fiche.to_dict())


