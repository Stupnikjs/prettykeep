import unittest
import requests
import os
from sqlalchemy import create_engine, text
import sys
sys.path.append(os.getcwd())

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
        # CREATE TABLES 
        
    def test_base_url(self):
        r = self.client.get('/')
        assert r.status_code == 200, "status code should be 200"
    
    def test_get_fiche(self): 
        fiche = {
                "title": "test", 
                "text" : "test", 
                "created": "test", 
                "updated": "test",
                "complete_start": "test",
                "complete_end":"test"
        }            
        with engine.connect() as conn:  
            conn.execute(text(insert_new_fiche), fiche)
            conn.execute(text(insert_new_fiche), fiche)
            conn.execute(text(insert_new_fiche), fiche)
            conn.commit()
            r = self.client.get('/fiche/3')
            assert r.status_code == 200, "status code should be 200"
            # DELETE 
            conn.execute(text('DROP '))  
            


if __name__ == "__main__":
    unittest.main()
