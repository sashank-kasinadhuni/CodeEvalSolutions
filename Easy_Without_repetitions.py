import argparse


def Without_Repetitions():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    with open(args.filename) as f:
        for line in f:
            line = line.rstrip('\n')
            prev = ''
            result = ''
            for i in line:
                if i != prev:
                    result += i
                    prev = i
            print(result)
Without_Repetitions()
