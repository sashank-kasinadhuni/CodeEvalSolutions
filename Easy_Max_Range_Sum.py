import argparse


def Max_Range_Sum():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    with open(args.filename) as f:
        for line in f:
            line = line.rstrip('\n')
            line = line.split(';')
            line[1] = [int(i) for i in line[1].split()]
            max_sum = 0
            curr_sum = 0
            for i in range(0, len(line[1]) - int(line[0])+1):
                curr_sum = sum(line[1][i:i + int(line[0])])
                max_sum = max_sum if max_sum > curr_sum else curr_sum
            print(max_sum)
Max_Range_Sum()
