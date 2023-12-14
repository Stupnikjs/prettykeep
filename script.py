'''
import zipfile
import os
import json
import argparse


parser = argparse.ArgumentParser()

parser.add_argument('-p', '--path', required=True, help='Specify the path')

arg = parser.parse_args()



def extract_gkeep(arg):
    if arg.endswith('.zip'):    
        with zipfile.ZipFile(arg, 'r') as zip_ref:
            zip_ref.extractall('unzipped')
    else: 
        print('no zip file found, processing unzipped file')

    main_path = arg

    main_dir_files = os.listdir('unzipped/takeout/keep')

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

extract_gkeep(arg.path)


main_path = 'unzipped/Takeout'
json_files = os.listdir(main_path)

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
'''

