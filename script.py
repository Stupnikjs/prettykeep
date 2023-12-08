import zipfile
import os
import shutil 

'''
with zipfile.ZipFile('takeout.zip', 'r') as zip_ref:
    zip_ref.extractall('unzipped')

'''

main_path = "unzipped/Takeout/keep"

mai_dir_files = os.listdir(main_path)


