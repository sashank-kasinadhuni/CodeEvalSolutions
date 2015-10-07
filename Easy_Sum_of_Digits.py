import argparse


def Sum_of_Digits():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    with open(args.filename) as f:
        for line in f:
            line = line.rstrip("\n")
            print(sum([int(k) for k in list(line)]))

Sum_of_Digits()            