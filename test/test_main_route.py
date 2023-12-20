import unittest
from app import create_app
import requests 



class BaseCase(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://127.0.0.1:5000"   

    def test_sample(self):
        r = requests.get(self.base_url)
        result = r.json()
        print(result) 
