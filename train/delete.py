import os, random
files = os.listdir('images')
num = int(0.25 * len(files))
for i in range(num):
     file = random.choice(files)
     txtfile = file[:-3] + 'txt'
     files.remove(file)
     os.remove('images/'+file)
     os.remove('labels/'+txtfile)
