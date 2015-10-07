import argparse


def Set_intersection():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    with open(args.filename) as f:
        for line in f:
            line = [x.split(',') for x in line.rstrip('\n').split(';')]
            result = [k for k in line[0] if k in line[0] and k in line[1]]
            print(','.join(result))

Set_intersection()
