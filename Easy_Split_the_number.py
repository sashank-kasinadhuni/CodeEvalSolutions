import argparse

def Split_the_Number():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    with open(args.filename) as f:
        for line in f:
            line = line.rstrip('\n')
            line = line.split()
            operator = ""
            left = 0 
            for i in line[1]:
            	if(i == '+' or i == '-'):
            		operator = i
            		break
            	else:
            		left+=1
            a = int(line[0][0:left])
            b = int(line[0][left:])
            result = a-b if operator == "-" else a+b
            print(result)			
Split_the_Number()            