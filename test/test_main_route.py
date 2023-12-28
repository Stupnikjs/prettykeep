import os
import sys
import json
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import unittest
from sqlalchemy import create_engine, text

from db.initdb import init_tables
from db.query import insert_new_fiche, update_fiche_query
from sqlalchemy import create_engine

from config import TestingConfig
from router.main_route import create_routes




from app import create_app




class BaseCase(unittest.TestCase):
    
    def setUp(self): 
        self.app = create_app(TestingConfig)
        self.base_url = "http://127.0.0.1:4000"
        self.client = self.app.test_client() 
        self.engine = create_engine(self.app.config['SQLALCHEMY_DATABASE_URI'])
        create_routes(self.app ,self.engine)
        init_tables(TestingConfig.TESTING, engine=self.engine)
        
        
    def test_base_url(self):
        r = self.client.get('/')
        assert r.status_code == 200, "status code should be 200"
    
    def test_get_fiche(self): 
        fiche = {
                "title": "test", 
                "text" : "test", 
                "created": "test", 
                "updated": "test",
                "complete_start": 0,
                "complete_end": 0,
        }            
        with self.engine.connect() as conn:  
            conn.execute(text(insert_new_fiche), fiche)
            conn.execute(text(insert_new_fiche), fiche)
            conn.execute(text(insert_new_fiche), fiche)
            conn.commit()
            r = self.client.get('/fiche/3')
            assert r.status_code == 200, "status code should be 200"
            # DELETE 
            conn.execute(text('TRUNCATE TABLE fiches CASCADE; '))
            conn.commit() 
    def test_update_fiche(self):
        fiche = {
                "title": "test", 
                "text" : "test", 
                "created": "test", 
                "updated": "test",
                "complete_start": 0,
                "complete_end": 0,
        }    
        update_fiche = fiche
        update_fiche['title'] = "modified"      
        with self.engine.connect() as conn: 

            conn.execute(text(insert_new_fiche), fiche)
            conn.execute(text(insert_new_fiche), fiche)
            conn.execute(text(insert_new_fiche), fiche)
            
            conn.commit()
            self.client.post('/updatefiche/3', json={ "fiche" : update_fiche})
            print('Response content:', r_after.get_data(as_text=True))

            # Try to retrieve JSON content
            updated_fiche = r_after.get_json()

            # Check if JSON content is None
            if updated_fiche is not None:
                # Assuming 'title' is the attribute you want to check
                assert updated_fiche['fiche']['title'] == 'modified', "title should be modified"
            else:
                print('Error: No JSON content in the response')
            assert r_after.get_json()['fiche'] == 'modified', ""
            # DELETE 
            conn.execute(text('TRUNCATE TABLE fiches CASCADE; '))
            conn.commit() 
            
if __name__ == "__main__":
    unittest.main()
