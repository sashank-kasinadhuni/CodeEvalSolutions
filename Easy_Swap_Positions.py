import argparse


def Swap_Indices():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    with open(args.filename) as f:
    	for line in f:
    		line = line.rstrip('\n')
    		line = line.split(':')
    		Numbers = line[0].split()
    		Indices = [i.split('-') for i in line[1].split(',')]
    		# print('Numbers: ',Numbers)
    		# print("Indices:",Indices)
    		for i in Indices:
    			temp = Numbers[int(i[0])]
    			Numbers[int(i[0])] = Numbers[int(i[1])]
    			Numbers[int(i[1])] = temp
    		print(" ".join(Numbers))
Swap_Indices()    			