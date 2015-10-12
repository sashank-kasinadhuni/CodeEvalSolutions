import argparse
from collections import Counter

def Major_Element():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    with open(args.filename) as f:
        for line in f:
            line = line.rstrip('\n')
            line = line.split(',')
            counts = Counter(line)
            val = counts.most_common(1)[0]
            print("{res}".format(res = val[0] if val[1]>=len(line)/2 else 'None'))
Major_Element()            