import argparse

def LetterCase_Percentage():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    with open(args.filename) as f:
        for line in f:
        	line = line.rstrip('\n')
        	total = len(line)
        	lower = 0
        	higher = 0
        	for i in line:
        		if ord(i)>=97 and ord(i)<= 122:
        			lower += 1
        		else:
        			higher+=1
        	print("lowercase: {:.2f} uppercase: {:.2f}".format(lower*100/total,higher*100/total))			
LetterCase_Percentage()        	