import unittest
from app import create_app
import requests 



class BaseCase(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://127.0.0.1:5000"


class TestMainRoute(unittest.TestCase):
    def setUp(self) -> None:
        

    
