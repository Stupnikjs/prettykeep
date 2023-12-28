from sqlalchemy import  text 
import os 


create_fiches_table_query = """
CREATE TABLE IF NOT EXISTS fiches ( 
    fiche_id SERIAL PRIMARY KEY, 
    title VARCHAR(20000), 
    text text, 
    created VARCHAR(20), 
    updated VARCHAR(20), 
    complete_start INTEGER, 
    complete_end INTEGER
);
"""

create_labels_table_query =  """
CREATE TABLE IF NOT EXISTS labels (
    label_id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    hot BOOLEAN
);


"""


create_link_table = """
CREATE TABLE IF NOT EXISTS link (
      link_id SERIAL PRIMARY KEY,
      fiche_id INT REFERENCES fiches(fiche_id),
      label_id INT REFERENCES labels(label_id)

);

"""

def init_tables(testing, engine):
        print(testing)
        with engine.connect() as conn:
            """
            if testing:
                conn.execute(text('DROP TABLE fiches CASCADE; DROP TABLE labels CASCADE; DROP TABLE link; '))
            """

            conn.execute(text(create_fiches_table_query))
            conn.execute(text(create_labels_table_query))
            conn.execute(text(create_link_table))
            conn.commit()

    
    

    




    


    








