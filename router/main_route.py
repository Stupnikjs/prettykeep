import base64
from flask import  render_template, request
from datetime import datetime
from sqlalchemy import text
from db.query import select_fiche_by_id, update_fiche_query, select_all_labels, select_fiches_by_label, select_light_fiche_by_label, select_all_fiches
from utils import special_decoder



def create_routes(app, engine):
    @app.route('/')
    def home():
        return render_template('home.html')

    # afficher la fiche 
    @app.route('/fiche/<int:id>')
    def get_fiche_by_id(id):
        
        with engine.connect() as conn:
            fiche = conn.execute(text(select_fiche_by_id), {"id": id }).first()
            return_obj = {}
            if fiche: 
                newtext = special_decoder(fiche[1])
                return_obj['title'] = fiche[0]
                return_obj['text'] = newtext
                return_obj['created'] = fiche[2]
                return_obj['updated'] = fiche[3]
                return_obj['complete_start'] = fiche[4]
                return_obj['complete_end'] = fiche[5]
                return_obj['labels'] = fiche[6]
                return_obj['id'] = id
                
            return render_template("fiche_by_id.html", fiche=return_obj)

     # afficher la fiche 
    @app.route('/allfiches')
    def get_all_fiches():
        with engine.connect() as conn:
            fiches = conn.execute(text(select_all_fiches)).fetchall()
            return_obj_list = []
            return_obj = {}
            for fiche in fiches: 
                newtext = special_decoder(fiche[1])
                return_obj['title'] = fiche[0]
                return_obj['text'] = newtext
                return_obj['created'] = fiche[2]
                return_obj['updated'] = fiche[3]
                return_obj['complete_start'] = fiche[4]
                return_obj['complete_end'] = fiche[5]
                return_obj['labels'] = fiche[6]
                return_obj['id'] = id
                return_obj_list.append(return_obj)    
            return render_template("fiche_roll.html", fiches=return_obj_list)
        
    @app.route('/labels/all')
    def all_labels():
        with engine.connect() as conn:
            labels = conn.execute(text(select_all_labels)).fetchall()
            return render_template('labels.html', labels=labels)

    # mettre a jour la fiche 
    @app.route('/updatefiche/<int:id>', methods=['POST'])
    def update_fiche(id):
        
        today = datetime.now().strftime("%d-%m-%Y %H:%M")  
        updated_fiche = request.get_json()['fiche']  
        updated_fiche['id'] = id
        print(updated_fiche)
        with engine.connect() as conn: 
            conn.execute(text(update_fiche_query), {
                "title": updated_fiche['title'],
                "text": updated_fiche['text'],
                "created": updated_fiche['created'],
                "updated": today,
                "complete_start": updated_fiche['complete_start'],
                "complete_end": updated_fiche['complete_end'],
                "id": updated_fiche['id']
            } )
            conn.commit()
            return updated_fiche
 
        # sql request 
     
    # all fiches with label 
    #
    @app.route('/label/<string:label>')
    def get_fiches_with_label(label):
        # with sql conn
        decoded_label = base64.urlsafe_b64decode(label).decode('utf-8')
        
        with engine.connect() as conn: 
            fiches = conn.execute(text(select_fiches_by_label), {'label':decoded_label}).fetchall()
            return_obj_list = []
            for fiche in fiches: 
                return_obj = {}
                newtext = special_decoder(fiche[1])
                return_obj['title'] = fiche[0]
                return_obj['text'] = newtext
                return_obj['created'] = fiche[2]
                return_obj['updated'] = fiche[3]
                return_obj['complete_start'] = fiche[4]
                return_obj['complete_end'] = fiche[5]
                return_obj['label'] = decoded_label
                return_obj['id'] = fiche[6]
                return_obj_list.append(return_obj)
            print("list ok", return_obj_list)
            return render_template("bylabel.html", fiches=return_obj_list)
    
    
    

    
    """
   


        

    

    # supprimer la fiche 
    @app.route('/deletefiche/<int:id>')
    def delete_fiche(id):
        # with sql conn
        with engine.connect() as conn:
            conn.execute(text(delete_by_id_query))
            conn.commit()


    """