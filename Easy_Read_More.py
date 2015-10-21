import argparse


def Read_More():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    with open(args.filename) as f:
        for line in f:
        	line = line.rstrip('\n')
        	if len(line)<=55:
        		print(line)
        	else :
        		line = line[:40]
        		idx = 39
        		while(line[idx]!=' ' and idx>=0):
        			idx -=1
        		line = line[:idx]
        		line+=	'... <Read More>'
        		print(line)	
Read_More()