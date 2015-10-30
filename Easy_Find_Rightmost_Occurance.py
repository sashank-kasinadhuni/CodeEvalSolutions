import argparse

def Index_finder():
	parser = argparse.ArgumentParser()
	parser.add_argument("filename")
	args = parser.parse_args()
	with open(args.filename) as f:
		for line in f:
			line = line.rstrip("\n")
			line = line.split(',')
			IDx = -1
			for i in range(0,len(line[0])):
				if line[0][i] == line[1]:
					IDx = i
		print(IDx)	
Index_finder()    			