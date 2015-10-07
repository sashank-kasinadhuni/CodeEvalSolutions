import argparse


def Lower_case():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    with open(args.filename) as f:
        for line in f:
            line = line.rstrip("\n")
            print(line.lower())

Lower_case()            