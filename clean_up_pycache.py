import os
import shutil


for x in os.walk('.'):
    if x[0].startswith('.\\.venv'):
        pass
    elif '__pycache__' in x[0]:
        print('Removing {}'.format(x[0]))
        shutil.rmtree(x[0])