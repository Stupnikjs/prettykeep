insert_new_fiche = """
INSERT INTO fiches (title,text, created, updated, complete_start, complete_end)
VALUES (:title, :text,  :created, :updated, :complete_start, :complete_end)
RETURNING fiche_id;
"""


select_label_with_name = """
SELECT * FROM labels 
WHERE name = :name
"""


create_label_with_name = """
INSERT INTO label (name, hot) 
VALUES (:name, :hot)
"""


insert_link = """
INSERT INTO link ( fiche_id, label_id)
VALUES (:fiche_id, :label_id)
"""