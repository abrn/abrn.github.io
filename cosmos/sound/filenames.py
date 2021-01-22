import os
import sys
import re
import shutil
import codecs

assetfiles = [f for f in os.listdir('.') if os.path.isfile(os.path.join('.', f))]

try:
    os.stat('./original')
except:
    os.mkdir('./original')

for file in assetfiles:
    if file.endswith('.wav'):
        print('Trying ' + file + '...')
        match = re.search(r'^([(A-z0-9\s)]+)(?!resources.assets\\-)', file)
        if match is not None:
            shutil.copyfile(r'./'+file, r'./original/'+file)
            shutil.copyfile(r'./'+file, r'./'+match.group()+'.wav') 
            os.remove(r'./'+file)