import argparse

def Compress_Numbers():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    with open(args.filename) as f:
        for line in f:
            line = line.rstrip('\n')
            line = line.split()
            count = 1
            prev = line[0]
            res = ""
            line.pop(0)
            for i in line:
            	if i == prev:
            		count += 1
            	else:
            		res= res+str(count)+" "+prev if res =="" else res + " "+ str(count)+ " "+prev
            		#print("res: ",res)
            		prev = i
            		count = 1
            res= res+str(count)+" "+prev if res =="" else res + " "+ str(count)+ " "+prev 			
            print(res)							
Compress_Numbers()            