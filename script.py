from datetime import datetime
import zipfile
import os
import json
import argparse
from sqlalchemy import create_engine, text
from query import insert_new_fiche, select_label_with_name, create_label_with_name, insert_link

parser = argparse.ArgumentParser()

parser.add_argument('-p', '--path', required=True, help='Specify the path')

arg = parser.parse_args()

uri= "postgresql://fxplwekm:pgZ9xU385QNotPsxUjAKq2MF72C8puRD@kandula.db.elephantsql.com/fxplwekm"
uri2 = "postgresql://vxxssqap:nX4LrcOIo9uQ1OQtPpXHm6PEm5MC_lDx@horton.db.elephantsql.com/vxxssqap"

engine = create_engine(uri2, pool_size=4, max_overflow=2)



def is_json(file):
    return file.endswith('.json')

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
                    data = json.load(json_file)  
                    labels = []
                    for dict in data['labels']:
                        print(dict['name'])
                        labels.append(dict['name'])
                    with engine.connect() as conn:

                        res = conn.execute(insert_new_fiche, 
                            (data['textContent'],
                            data['title'],
                            today,
                            None,
                            0,
                            0)
                        )
                        fiche_id = res.scalar()
                        
                        for label in labels:
                                label = conn.execute(select_label_with_name, label) 
                                if label == None:
                                    res_query  = conn.execute(create_label_with_name, label, id)
                                    label_id = res_query.scalar() 
                                conn.execute(insert_link , fiche_id, label_id)
                                
                except Exception as e: 
                    print(f'the exception is {e}')

extract_gkeep(arg.path)

with engine.connect() as conn:
    result = conn.execute(text('SELECT * FROM fiches')).fetchall()
    for row in result:
        print(row)
    result = conn.execute(text('SELECT * FROM association')).fetchall()
    for row in result:
        print(row)







        


