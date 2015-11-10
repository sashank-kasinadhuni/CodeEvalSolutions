import argparse


def Strings_and_Arrows():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    with open(args.filename) as f:
        for line in f:
            line = line.rstrip("\n")
            count = 0
            for i in range(0, len(line) - 4):
                #print(line [i:i+5])
                if line[i:i + 5] == '>>-->' or line[i:i + 5] == '<--<<':
                    count += 1
            print(count)
Strings_and_Arrows()
