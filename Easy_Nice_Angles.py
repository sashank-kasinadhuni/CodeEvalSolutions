import argparse


def Nice_Angles():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    with open(args.filename) as f:
        for line in f:
            val = float(line)
            degrees = int(val)
            minutes = (val - degrees) * 60
            seconds = (minutes - int(minutes)) * 60
            result = str(degrees)+'.' + str(int(minutes)).zfill(2) + \
                "'" + str(int(seconds)).zfill(2) + '"'
            print(result)

Nice_Angles()
