import argparse

def Hex_To_Decimal():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    myTable = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'a':10,'b':11,'c':12,'d':13,'e':14,'f':15}
    with open(args.filename) as f:
        for line in f:
        	line= line.rstrip('\n')
        	digits = list(line)[::-1]
        	multiplier = 1
        	base_10 = 0
        	for i in digits:
        		base_10 += myTable[i]*multiplier
        		multiplier *= 16
        	print(base_10)	
Hex_To_Decimal()        	