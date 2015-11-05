import argparse


def Minimum_Distance():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    with open(args.filename) as f:
        for line in f:
            line = line.rstrip('\n')
            line = [int(i) for i in line.split()]
            val = int(sum(line[1:])/len(line[1:]))
            #print("val: ",val)
            diff = 0
            for i in range(1,len(line)):
            	diff += abs(line[i] - val)
            	#print (abs(line[i] - val),end = ",")
            print(diff)
Minimum_Distance()