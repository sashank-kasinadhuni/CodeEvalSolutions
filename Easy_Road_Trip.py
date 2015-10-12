import argparse

def Road_Trip():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    with open(args.filename) as f:
        for line in f:
            line = line.rstrip('\n')
            line = [int(k) for i in line.split(';') if i!='' for k in i.split(',') if k.isnumeric()]
            line.sort()
            result = [str(line[i]) if i==0 else str(line[i] - line[i-1]) for i in range(0,len(line))]
            print(",".join(result))
Road_Trip()						        	