import argparse

def Details():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    with open(args.filename) as f:
        for line in f:
        	line = line.rstrip('\n')
        	line = line.split(',')
        	diff = len(line[0])
        	for row in line:
        		Rx,Ly = 0,len(line[0])
        		for k in range(0,len(row)) :
        			if row[k] =="X" and k>Rx:
        				Rx = k
        			elif row[k] =="Y":
        				Ly = k
        				diff = diff if Ly-Rx-1>diff else Ly-Rx-1
        				break
        	print(diff)				
Details()        		