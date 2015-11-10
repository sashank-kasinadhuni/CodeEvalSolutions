import argparse


def String_Mask():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    with open(args.filename) as f:
        for line in f:
            line = line.rstrip("\n")
            line = line.split()
            res = ''
            for i in range(0,len(line[0])):
            	res = res+line[0][i] if line[1][i] == '0' else res+line[0][i].upper()
            print(res)
String_Mask()            