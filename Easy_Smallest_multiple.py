import argparse

def Mult_finder():
	parser = argparse.ArgumentParser()
	parser.add_argument("filename")
	args = parser.parse_args()
	with open(args.filename) as f:
		for line in f:
			line = line.rstrip('\n')
			Numbers = [int(x) for x in line.split(',')]
			Base = Numbers[1]
			Limit = Numbers[0]
			output = Base
			while(output<Limit):
				output += Base
			print(output)	

Mult_finder()	