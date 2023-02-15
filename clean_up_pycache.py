import os

for x in os.walk('.'):
    if '__pycache__' in x[0]:
        print('Removing {}'.format(x[0]))
        os.removedirs(x[0])