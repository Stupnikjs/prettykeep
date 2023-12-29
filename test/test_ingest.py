import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import unittest
from sqlalchemy import create_engine, text

from db.initdb import init_tables
from db.query import insert_new_fiche, insert_label_with_name, insert_link
from sqlalchemy import create_engine

from config import TestingConfig

from router.main_route import create_routes

from app import create_app






class test_ingest(unittest.TestCase):
    
    def setUp(self): 
        self.app = create_app(TestingConfig)
        self.base_url = "http://127.0.0.1:4000"
        self.client = self.app.test_client() 
        self.engine = create_engine(self.app.config['SQLALCHEMY_DATABASE_URI'], pool_size=3)
        create_routes(self.app ,self.engine)
        init_tables(TestingConfig.TESTING, engine=self.engine)

    def tearDown(self):
        self.engine.dispose()   

    
    
     
            
if __name__ == "__main__":
    unittest.main()
