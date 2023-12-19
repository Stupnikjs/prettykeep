from sqlalchemy import create_engine, text 
import os 


create_fiches_table_query = """
CREATE TABLE IF NOT EXISTS fiches ( 
    fiche_id SERIAL PRIMARY KEY, 
    title VARCHAR(20000), 
    text VARCHAR(20000), 
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

if 'DB_URI' in os.environ: 
    uri=os.environ['DB_URI']
else: 
    uri="postgresql://vxxssqap:nX4LrcOIo9uQ1OQtPpXHm6PEm5MC_lDx@horton.db.elephantsql.com/vxxssqap"

engine = create_engine(uri)




with engine.connect() as conn:
    conn.execute(text('DROP TABLE fiches CASCADE; DROP TABLE labels CASCADE; DROP TABLE link; '))
    conn.execute(text(create_fiches_table_query))
    conn.execute(text(create_labels_table_query))
    conn.execute(text(create_link_table))
    conn.commit()
    








