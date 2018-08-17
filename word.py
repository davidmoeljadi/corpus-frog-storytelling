import codecs
import glob
import os

path = '/data/written'

for filename in glob.glob(os.path.join(path, '*.txt')):
    f = codecs.open(filename, encoding='utf-8', mode='r')
    for line in f.readlines():
        items = line.strip()

items[0]
