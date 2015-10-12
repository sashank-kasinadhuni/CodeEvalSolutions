import argparse

def Camel_Case():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    with open(args.filename) as f:
        for line in f:
        	line = line.rstrip('\n')
        	base_string = ""
        	toUpper = True
        	for i in line:
        		if (toUpper):
        			if (i.isalpha()):
        				base_string += i.upper()
        			else:
        				base_string +=	i
        			toUpper = False
        		else:
        			base_string += i
        			if i ==" ":
        				toUpper = True
        	print (base_string)
Camel_Case()        						