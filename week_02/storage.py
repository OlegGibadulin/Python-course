import os
import tempfile
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--key', action="store", dest="key_name")
parser.add_argument('--val', action="store", dest="value", default=None)

args = parser.parse_args()

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

with open(storage_path, 'a') as f:
    pass

if (args.key_name == None):
    exit()

if (args.value == None):
    count = 0
    line = []
    with open(storage_path, 'r') as f:
        line_key = str(f.readline())[:-1:]
        while (line_key != ''):
        	if (line_key == str (args.key_name) and count % 2 == 0):
        		line.append(str(f.readline())[:-1:])
        		count += 1
        	else:
        		f.readline()
        		count += 1
        	count += 1
        	line_key = str(f.readline())[:-1:]

    str = ""
    for i in range(len(line)):
    	str += line[i]
    	if (i + 1 != (len(line))):
    		str += ", "

    print(str)
else:
    with open(storage_path, 'a') as f:
        f.write(str(args.key_name) + "\n")
        f.write(str(args.value) + "\n")
