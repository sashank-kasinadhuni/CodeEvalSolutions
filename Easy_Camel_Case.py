import argparse

def Camel_Case():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    with open(args.filename) as f:
        for line in f:
        	line = line.rstrip('\n')
        	print("".join(x for x in line.title() ))
Camel_Case()        	