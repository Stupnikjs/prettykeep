from datetime import datetime
import zipfile
import os
import json
import argparse
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session 
from orm import Fiche, Base,Label
import sys

parser = argparse.ArgumentParser()

parser.add_argument('-p', '--path', required=True, help='Specify the path')

arg = parser.parse_args()

uri= "postgresql://fxplwekm:pgZ9xU385QNotPsxUjAKq2MF72C8puRD@kandula.db.elephantsql.com/fxplwekm"
uri2 = "postgresql://vxxssqap:nX4LrcOIo9uQ1OQtPpXHm6PEm5MC_lDx@horton.db.elephantsql.com/vxxssqap"

engine = create_engine(uri2, pool_size=4, max_overflow=2)




if arg.path == "reset":
    Base.metadata.drop_all(engine)
    sys.exit()

else :
    Base.metadata.create_all(engine, checkfirst=True)


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
                    with Session(engine) as session:
                        fiche = Fiche(
                            text = data['textContent'],
                            title = data['title'],
                            created = today,
                            updated = None,
                            complete_start = 0,
                            complete_end = 0
                        )
                        
                        for label in labels:
                                label = session.query(Label).filter(Label.name == label).first()
                                if label == None: 
                                    label_instance =  Label(
                                        name = label,
                                        hot = False
                                    )
                                else: 
                                    label_instance = label
                                fiche.labels.append(label_instance)
                        session.add(fiche)
                        session.commit()
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







        


