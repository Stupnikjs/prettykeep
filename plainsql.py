create_table_fiche_query = """
'CREATE TABLE  IF NOT EXISTS fiches ( 
    id INTEGER NOT NULL, 
    title VARCHAR(200), 
    text VARCHAR(2000), 
    created VARCHAR(20), 
    updated VARCHAR(20), 
    complete_start INTEGER, 
    complete_end INTEGER,
    PRIMARY KEY (id)
);'
"""

print(create_table_fiche_query)

