import argparse

def Hidden_Numbers():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    with open(args.filename) as f:
        for line in f:
        	line = line.rstrip('\n')
        	result = ""
        	for i in line:
        		if(ord(i)>=48 and ord(i)<=57):
        			result+=i
        		elif(ord(i)>=97 and ord(i)<=106):
        			result+= str(ord(i) - 97)	
        	print("{res}".format(res = result if len(result)>0 else "NONE"))
Hidden_Numbers()        	