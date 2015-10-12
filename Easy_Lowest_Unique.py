import argparse

def Lowest_Unique():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    with open(args.filename) as f:
        for line in f:
        	line = line.rstrip('\n')
        	line = [int(i) for i in line.split()]
        	counts = dict()
        	for i in line:
        		if i in counts:
        			counts[i] += 1
        		else :
        			counts[i] = 1
        	print(counts)		
        	min_Idx = -1
        	for idx in range(0,len(line)):
        		if (counts[line[idx]] == 1):
        			if(min_Idx == -1):
        				min_Idx = idx
        			else:
        				min_Idx = min_Idx if line[min_Idx]<line[idx] else idx
        	print(min_Idx+1)							
Lowest_Unique()        	