insert_new_fiche = """
INSERT INTO fiches (title, text, created, updated, complete_start, complete_end)
VALUES (:title, :text,  :created, :updated, :complete_start, :complete_end)
RETURNING fiche_id;
"""


select_label_with_name = """
SELECT * FROM labels 
WHERE name = :name
"""


create_label_with_name = """
INSERT INTO labels (name, hot) 
VALUES (:name, :hot)
RETURNING label_id
"""


insert_link = """
INSERT INTO link ( fiche_id, label_id)
VALUES (:fiche_id, :label_id)
"""


select_fiche_by_label  = """
   SELECT f.title, f.text 
   FROM fiches f
   JOIN link l ON f.fiche_id = l.fiche_id
   JOIN labels la ON l.label_id = la.label_id
   WHERE la.name = :label;
   
"""