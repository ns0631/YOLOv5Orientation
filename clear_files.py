#Clear all files
import os

for dir in ['test', 'train', 'valid']:
    for category in ['images', 'labels']:
        files = os.listdir(f'./{dir}/{category}/')
        for file in files:
            if 'txt' in file or 'png' in file:
                os.remove(f'./{dir}/{category}/{file}')
