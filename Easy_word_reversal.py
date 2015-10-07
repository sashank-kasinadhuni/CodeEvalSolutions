import argparse


def Word_reverser():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    with open(args.filename) as f:
        for line in f:
            line = line.rstrip("\n")
            print(' '.join(line.split(' ')[::-1]))

Word_reverser()