from datetime import datetime
import zipfile
import os
import json
import argparse
from sqlalchemy import create_engine, text
from db.query import insert_new_fiche, select_label_with_name, create_label_with_name, insert_link
import traceback


parser = argparse.ArgumentParser()
parser.add_argument('-p', '--path', required=True, help='Specify the path')
arg = parser.parse_args()



uri = "postgresql://vxxssqap:nX4LrcOIo9uQ1OQtPpXHm6PEm5MC_lDx@horton.db.elephantsql.com/vxxssqap"
engine = create_engine(uri, pool_size=4, max_overflow=2)



def is_json(file):
    return file.endswith('.json')


def load_json(file): 
    try:
        data = json.load(file)
        labels = []
        if 'labels' in data:
            for label in data['labels']:
                labels.append(label['name'])
            data['labels'] = labels
        return data
    except Exception as e: 
        print(e)
        return None
        



def extract_gkeep(arg):
    if arg.endswith('.zip'):    
        with zipfile.ZipFile(os.path.join(os.getcwd(), arg), 'r') as zip_ref:
            zip_ref.extractall('unzipped')
    else: 
        print('no zip file found, processing unzipped file')
    
    json_files = filter(is_json,os.listdir(os.path.join( os.getcwd(), "unzipped","takeout", "keep")))
    today = datetime.now().strftime("%d-%m-%Y %H:%M")

    for json_file_path in json_files:
        with open(os.path.join( os.getcwd(), "unzipped","takeout", "keep" , json_file_path)) as json_file:
                try:
                    data = load_json(json_file) 
                    if data is None: 
                        continue
                    with engine.connect() as conn:
                        insert = {
                            'title': data['title'],
                            'text': data['textContent'],
                            'created': today,
                            'updated': None,
                            'complete_start': 0,
                            'complete_end':0
                        
                        }
                        res = conn.execute(text(insert_new_fiche), insert)
                        fiche_id = res.scalar()
                        print(fiche_id)
                        if 'labels' in data:
                            for label in data['labels']:
                                res_search = conn.execute(text(select_label_with_name), {'name': label}).first()
                                
                                if res_search is None:
                                    res_query  = conn.execute(text(create_label_with_name), {"name":label, "hot": False})
                                    label_id = res_query.scalar()
                                    conn.execute(text(insert_link) , {"fiche_id": fiche_id, "label_id":label_id})
                                else: 
                                    label_id = res_search[1]
                                    conn.execute(text(insert_link) , {"fiche_id": fiche_id, "label_id":label_id})
                        conn.commit()
                except: 
                     traceback.print_exc()              

extract_gkeep(arg.path)









        


