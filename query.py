insert_new_fiche = """
INSERT INTO fiche (text, title, created, updated, complete_start, complete_end)
VALUES (:text, :title, :created, :updated, :complete_start, :complete_end);
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
INSERT INTO LINK ( fiche_id, label_id)
VALUES (:fiche_id, :label_id)
"""