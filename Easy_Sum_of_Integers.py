import argparse


def Sum_of_Integers():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    sum_val = 0
    with open(args.filename) as f:
        for line in f:
            line = line.rstrip('\n')
            sum_val += int(line)
        print(sum_val)    
Sum_of_Integers()           