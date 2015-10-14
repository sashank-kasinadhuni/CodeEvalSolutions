import argparse

def Data_Recovery():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    with open(args.filename) as f:
        for line in f:
            line = line.rstrip('\n')
            line = [[a for a in i.split()]for i in line.split(';')]
            res = ['' for i in range(0,len(line[0]))]
            #print("we have : ",len(line[1]))
            for i in range(0,len(line[0])):
            	#print(int(line[1][i])-1,line[0][i]
            	if i< len(line[1]):
            		res[int(line[1][i])-1] = line[0][i]
            		#print(res)
            	else:
            		res[res.index('')] = line[0][i]		
            res[:] = [i for i in res if i!='']
            print(" ".join(res))
Data_Recovery()            