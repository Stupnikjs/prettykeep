import zipfile
import os
import shutil 
import json
import pathlib

'''
with zipfile.ZipFile('takeout.zip', 'r') as zip_ref:
    zip_ref.extractall('unzipped')

'''

main_path = "unzipped/Takeout/keep"

main_dir_files = os.listdir(main_path)

json_files = []
for file in main_dir_files:
    if file.endswith('.json'):
        json_files.append(file)

print(len(json_files))


# open a json file 
relevant = []
for json_file_path in json_files:
    with open(os.path.join(main_path, json_file_path)) as json_file:
        try :
            data = json.load(json_file)
            obj = {}
            obj['text'] = data['textContent']
            obj['title'] = data['title']
            obj['labels'] = data['labels'][0]['name']
            relevant.append(obj)
        except Exception as e:
            print(e)

