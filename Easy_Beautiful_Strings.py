import argparse
from collections import Counter


def Beautiful_Strings():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    with open(args.filename) as f:
        for line in f:
        	line= line.rstrip('\n')
        	line = list(line.lower())
        	line[:] =[i for i in line if i.isalpha()]
        	counts = Counter(line)
        	total_score = 0
        	base = 26
        	for i in counts.most_common(26):
        		total_score += base*i[1]
        		base -= 1
        	print(total_score)	
Beautiful_Strings()