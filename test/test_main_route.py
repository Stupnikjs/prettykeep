import unittest
import requests

from app import create_app 



class BaseCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app("fiche_blueprint")
        self.base_url = "http://127.0.0.1:5000"   

    def test_sample(self):
        r = requests.get(self.base_url)
        assert r.status_code == 200, "status code should be 200"

    

if __name__ == "__main__":
    BaseCase.app.run()
    unittest.main()