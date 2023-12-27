insert_new_fiche = """
INSERT INTO fiches (title, text, created, updated, complete_start, complete_end)
VALUES (:title, :text,  :created, :updated, :complete_start, :complete_end)
RETURNING fiche_id;
"""


select_label_with_name = """
SELECT name,label_id  FROM labels 
WHERE name = :name;
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


select_light_fiche_by_label  = """
   SELECT f.title, f.text, f.fiche_id 
   FROM fiches f
   JOIN link l ON f.fiche_id = l.fiche_id
   JOIN labels la ON l.label_id = la.label_id
   WHERE la.name = :label;
   
"""


select_fiche_by_id = """
SELECT f.title, f.text, f.created, f.updated, f.complete_start, f.complete_end, la.name 
 FROM fiches f 
 LEFT JOIN link l ON f.fiche_id = l.fiche_id
 LEFT JOIN labels la ON l.label_id = la.label_id
 WHERE f.fiche_id = :id;
"""

select_all_fiches = """
SELECT f.title, f.text, f.created, f.updated, f.complete_start, f.complete_end, la.name 
 FROM fiches f 
 LEFT JOIN link l ON f.fiche_id = l.fiche_id
 LEFT JOIN labels la ON l.label_id = la.label_id;
 
"""

# not working returning only one entry multiple time 

select_fiches_by_label = """
SELECT f.title, f.text, f.created, f.updated, f.complete_start, f.complete_end, f.fiche_id 
 FROM fiches f 
  JOIN link l ON f.fiche_id = l.fiche_id
  JOIN labels la ON l.label_id = la.label_id
  WHERE la.name = :label
  ;

"""

"""
SELECT f.title, f.text, f.fiche_id , la.name FROM fiches f JOIN link l ON f.fiche_
 id = l.fiche_id JOIN labels la ON la.label_id = l.label_id WHERE la.name = 'Python' 
"""


update_fiche_query = """
UPDATE fiches 
SET title = :title , 
   text = :text, 
   created = :created, 
   updated = :updated, 
   complete_start = :complete_start, 
   complete_end = :complete_end 
WHERE fiche_id = :id ;
   """

select_all_labels = """
SELECT l.name, l.hot 
FROM labels l 
"""

delete_by_id_query = """
DELETE FROM link WHERE fiche_id = :id;
DELETE from fiches WHERE fiche_id = :id; 
"""