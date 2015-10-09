import argparse

def Penultimate_Word():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    with open(args.filename) as f:
        for line in f:
        	line = line.rstrip('\n')
        	line = line.split()
        	print(line[len(line)-2])
Penultimate_Word()        	