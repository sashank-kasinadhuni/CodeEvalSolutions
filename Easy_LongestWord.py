import argparse


def Longest_Word():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    with open(args.filename) as f:
    	for line in f:
    		line = line.rstrip('\n')
    		line = line.split()
    		longest_word = ""
    		for i in line:
    			if(len(i) > len(longest_word)):
    				longest_word = i
    		print(longest_word)
Longest_Word()    				
