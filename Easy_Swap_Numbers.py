import argparse


def Swap_Numbers():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    with open(args.filename) as f:
        for line in f:
            line = line.split()
            res = [i[-1]+i[1:len(i)-1]+i[0] for i in line]
            print (" ".join(res))

Swap_Numbers()            