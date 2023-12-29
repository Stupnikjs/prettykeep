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




class test_main_route(unittest.TestCase):
    
    def setUp(self): 
        self.app = create_app(TestingConfig)
        self.base_url = "http://127.0.0.1:4000"
        self.client = self.app.test_client() 
        self.engine = create_engine(self.app.config['SQLALCHEMY_DATABASE_URI'], pool_size=3)
        create_routes(self.app ,self.engine)
        init_tables(TestingConfig.TESTING, engine=self.engine)

    def tearDown(self):
        self.engine.dispose()   

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
        label = {
            "name": "Python",
            "hot": True,
        }       
        with self.engine.connect() as conn:
            res_fiche = conn.execute(text(insert_new_fiche), fiche)
            res_label = conn.execute(text(insert_label_with_name), {"name": label['name'], "hot": label['hot']} )
            fiche_id = res_fiche.scalar()
            label_id = res_label.scalar()
            conn.execute(text(insert_link), {"fiche_id": fiche_id, "label_id": label_id} )
            conn.commit()
            r = self.client.get('/fiche/109')
            assert r.status_code == 200, "status code should be 200"
            
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
            res_last = conn.execute(text(insert_new_fiche), fiche)
            last_id = res_last.scalar()
            conn.commit()


            self.client.post('/updatefiche/3', json={ "fiche" : update_fiche})
            r_after = self.client.get(f'/fiche/{last_id}')
            r_content = r_after.get_data(as_text=True)
            json_pos = r_content.find("data-fiche")
            last_item_pos = r_content.find("}")
            json_resp = r_content[json_pos: json_pos + last_item_pos + 10]
            assert json_resp[125:133] == 'modified', "modified field should equal modified"
            
            
            # EMPTY TABLES 
            conn.execute(text('TRUNCATE TABLE fiches CASCADE; '))
            conn.commit()
    
    def test_delete_fiche(self):
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
            res_last = conn.execute(text(insert_new_fiche), fiche)
            last_id = res_last.scalar()
            conn.commit()

            r_after = self.client.get(f'/fiche/{last_id}')
            print(r_after.get_data(as_text=True))
            self.client.get(f'/deletefiche/{last_id}')
            
            r_after_delete = self.client.get(f'/fiche/{last_id}')
            err_start = r_after_delete.get_data(as_text=True).find("id not found")
            assert err_start != -1



     
            
if __name__ == "__main__":
    unittest.main()
