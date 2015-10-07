import argparse

def Bit_manipulation():
	parser = argparse.ArgumentParser()
	parser.add_argument("filename")
	args = parser.parse_args()
	with open(args.filename) as f:
		for line in f:
			line = line.rstrip('\n')
			Numbers = [int(x) for x in line.split(',')]
			x = Numbers[0] & (1 << Numbers[1]-1)
			y = Numbers[0] & (1 << Numbers[2]-1)
			if ((x!=0 and y!=0) or (x==0 and y==0)):
				print('true')
			else:
				print('false')	


Bit_manipulation()