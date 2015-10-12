import argparse


def Mixed_Content():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    with open(args.filename) as f:
    	for line in f:
    		line = line.rstrip('\n')
    		line = line.split(',')
    		# print(line)
    		text = [i for i in line if i.isalpha()]
    		numbers = [i for i in line if i.isnumeric()]
    		# print(text)
    		# print(numbers)
    		print(",".join(text),'|',','.join(numbers))
Mixed_Content()    		