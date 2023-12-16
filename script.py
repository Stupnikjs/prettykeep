from datetime import datetime
import zipfile
import os
import json
import argparse
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session 
from model import Fiche

parser = argparse.ArgumentParser()

parser.add_argument('-p', '--path', required=True, help='Specify the path')

arg = parser.parse_args()

uri= "postgresql://qedivgso:GlAGhCxeJjsTKv_MoVz35OAjyxCXTeS9@tyke.db.elephantsql.com/qedivgso"

engine = create_engine(uri)

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
                    fiche = Fiche(
                        text = data['textContent'],
                        title = data['title'],
                        labels = data['labels'][0]['name'],
                        created = today,
                        updated = None,
                        complete_start = 0,
                        complete_end = 0
                    )
                
                    with Session(engine) as session:
                        session.add(fiche)
                        session.commit()
                except Exception as e: 
                    print(e)

extract_gkeep(arg.path)

with engine.connect() as conn:
    result = conn.execute(text('SELECT * FROM fiches')).fetchall()
    for row in result:
        print(row)




        


