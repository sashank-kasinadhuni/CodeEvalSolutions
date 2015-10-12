import argparse

def Find_Writer():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    with open(args.filename) as f:
        for line in f:
        	line = line.rstrip('\n')
        	line = line.split("|")
        	if (len(line) == 1):
        		continue
        	line[1] = [int(i) for i in line[1].split()]
        	#print(len(line[0]),max(line[1]))
        	Name = list()
        	for i in line[1]:
        		Name.append(line[0][i-1])
        	print("".join(Name))	
Find_Writer()       	