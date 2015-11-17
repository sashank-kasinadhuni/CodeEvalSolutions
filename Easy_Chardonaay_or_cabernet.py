import argparse


def Chardonnay_or_cabernet():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    with open(args.filename) as f:
        for line in f:
            line = line.rstrip("\n")
            line = line.split('|')
            line[0] = line[0].split()
            line[1] = line[1][1:]
            res = list()
            for i in line[0]:
                valid_matches = 0
                for k in line[1]:
                    if(k in i):
                        valid_matches += 1
                if valid_matches == len(line[1]):
                    res.append(i)
            if (len(res) == 0):
                print('False')
            else:
                print(" ".join(res))
Chardonnay_or_cabernet()
