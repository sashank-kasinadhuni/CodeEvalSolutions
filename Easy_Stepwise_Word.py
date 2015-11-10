import argparse


def Stepwise_Word():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    with open(args.filename) as f:
        for line in f:
            line = line.rstrip("\n")
            line = line.split()
            word = ""
            for i in line:
            	if(len(word)<len(i)):
            		word = i
            res = list()
            for i in range(0,len(word)):
            	letter = i*'*'+word[i]
            	res.append(letter)
            print(" ".join(res))			
Stepwise_Word()            	