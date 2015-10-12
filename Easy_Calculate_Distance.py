import argparse
from math import sqrt

def distance(List):
    return sqrt((List[0] - List[2])**2 + (List[1] - List[3])**2)


def parseInt(myStr):
    res = ""
    for i in myStr:
        if (i.isnumeric() or i == '-'):
            res += i
    return int(res)


def Calculate_Distance():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    with open(args.filename) as f:
        for line in f:
            line = line.rstrip('\n')
            line = line.split()
            line = [parseInt(res) for res in line]
            print(int(distance(line)))
Calculate_Distance()
