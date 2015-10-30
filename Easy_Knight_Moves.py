import argparse

def Knight_Moves():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    col = ["a","b","c","d","e","f","g","h"]
    row = ["1","2","3","4","5","6","7","8"]
    with open(args.filename) as f:
        for line in f:
        	line = line.rstrip('\n')
        	line = list(line)
        	# print(line)
        	r = row.index(line[1])
        	c = col.index(line[0])
        	# print(r,",",c)
        	res = list()
        	if(c - 2>=0):
        		if(r - 1>=0 ):
        			res.append(col[c-2]+row[r-1])
        		if(r+1<8):
        			res.append(col[c-2]+row[r+1])
        	if (c-1>=0):
        		if(r - 2>=0 ):
        			res.append(col[c-1]+row[r-2])
        		if(r+2<8):
        			res.append(col[c-1]+row[r+2])
        	if(c + 1<8):
        		if(r - 2 >= 0 ):
        			res.append(col[c+1]+row[r-2])
        		if(r+2<8):
        			res.append(col[c+1]+row[r+2])
        	if (c+2<8):
        		if(r - 1>=0 ):
        			res.append(col[c+2]+row[r-1])
        		if(r+1<8):
        			res.append(col[c+2]+row[r+1])
        	print(" ".join(res))		
Knight_Moves()