import unittest
import requests
import os

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
        
        
    def test_base_url(self):
        r = self.client.get('/')
        assert r.status_code == 200, "status code should be 200"
    
    def test_get_fiche(self): 
        r = self.client.get('/fiche/3')
        assert r.status_code == 200, "status code should be 200"


if __name__ == "__main__":
    unittest.main()
