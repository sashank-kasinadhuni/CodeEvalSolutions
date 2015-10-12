import argparse

def Even_Odd():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    with open(args.filename) as f:
        for line in f:
        	line = line.rstrip('\n')
        	print((int(line)%2)^1)
Even_Odd()        	