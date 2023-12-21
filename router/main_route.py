import base64
from flask import  render_template, request
from datetime import datetime
from sqlalchemy import text
from db.query import select_fiche_by_id, update_fiche_query, select_all_labels
from utils import special_decoder



def create_routes(app, engine):
    @app.route('/')
    def test():
        return 'hello'

    # afficher la fiche 
    @app.route('/fiche/<int:id>')
    def get_fiche_by_id(id):
        
        with engine.connect() as conn:
            fiche = conn.execute(text(select_fiche_by_id), {"id": id }).first()
            return_obj = {}
            if fiche: 
                print(fiche)
                newtext = special_decoder(fiche[1])
                return_obj['title'] = fiche[0]
                return_obj['text'] = newtext
                return_obj['created'] = fiche[2]
                return_obj['updated'] = fiche[3]
                return_obj['complete_start'] = fiche[4]
                return_obj['complete_end'] = fiche[5]
                return_obj['labels'] = fiche[6]
                
            return render_template("fiche.html", fiche=return_obj)

    # afficher la fiche 
    @app.route('/labels/all')
    def all_labels():
        with engine.connect() as conn:
            labels = conn.execute(text(select_all_labels)).fetchall()
            return render_template('labels.html', labels=labels)

    # mettre a jour la fiche 
    @app.route('/updatefiche/<int:id>', methods=['POST'])
    def update_fiche(id):
        # with sql conn
        today = datetime.now().strftime("%d-%m-%Y %H:%M")
        # champ update dans l'objet qui correspond  
        with engine.connect() as conn:
            updated_fiche = request.get_json()['fiche']
            # gérer erreur dans le json 
            updated_fiche['updated'] = today
        
        with engine.connect() as conn: 
            fiche = conn.execute(text(update_fiche_query))
            return fiche.first()
            """
            fiche = Fiche(
            title=updated_fiche['title'],
            text=updated_fiche['text'],
            labels=updated_fiche['labels'],
            created=updated_fiche['created'],
            updated=updated_fiche['updated'], 
            complete_start=updated_fiche['complete_start'],
            complete_end=updated_fiche['complete_end']
            )
            """
        
        # sql request 
    
    """
    # tous les labels 
    @app.route('/withlabel/<string:label>')
    def get_fiche_with_label(label):
        # with sql conn
        decoded_label = base64.urlsafe_b64decode(label)
        decoded_label = decoded_label[0].upper() + decoded_label[1:]
        with Session(engine) as session: 
            fiches = session.query(Fiche).filter_by(labels=decoded_label)
            return_fiches = []
            for fiche in fiches:   
                return_fiches.append(fiche.to_dict())
            print(return_fiches)
            return render_template("bylabel.html", fiches=return_fiches)


        

    

    # supprimer la fiche 
    @app.route('/deletefiche/<int:id>')
    def delete_fiche(id):
        # with sql conn
        with engine.connect() as conn:
            conn.execute(text(delete_by_id_query))
            conn.commit()


    """