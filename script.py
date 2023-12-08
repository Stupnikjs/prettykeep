import zipfile
import os
import shutil 
import json

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


