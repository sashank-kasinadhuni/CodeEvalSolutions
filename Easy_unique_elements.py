import argparse


def Unique_Elements():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    with open(args.filename) as f:
        for line in f:
            line = line.rstrip('\n').split(',')
            result = []
            for i in line:
            	if(i not in result):
            		result.append(i)
            #result.sort()		 
            print(','.join(result))
Unique_Elements()
