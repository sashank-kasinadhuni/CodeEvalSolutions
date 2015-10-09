import argparse

def Mod_Operator():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    with open(args.filename) as f:
        for line in f:
        	line= line.rstrip('\n')
        	numbers = [int(i) for i in line.split(',')]
        	quotient = numbers[0]//numbers[1]
        	print(numbers[0] - quotient*numbers[1])
Mod_Operator()        	