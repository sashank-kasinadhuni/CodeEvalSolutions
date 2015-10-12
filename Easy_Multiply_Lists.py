import argparse


def Multiply_Lists():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    with open(args.filename) as f:
    	for line in f:
    		line = line.rstrip('\n')
    		line = line.split("|")
    		listA = line[0].split()
    		listB = line[1].split()
    		# print(listA)
    		# print(listB)
    		result = list()
    		for i in range (0,len(listA)):
    			result.append(str(int(listA[i])*int(listB[i])))
    		print(" ".join(result))	
Multiply_Lists()    		