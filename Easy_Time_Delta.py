import argparse


def Delta_Time():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    with open(args.filename) as f:
        for line in f:
            line = [i.split(':') for i in line.split()]
            line[:] = [int(i[0])*3600+int(i[1])*60+int(i[2]) for i in line]
            diff = abs(line[0] - line[1])
            hours = diff // 3600
            diff %= 3600
            minutes = diff//60
            diff%=60
            seconds = diff
            result = str(hours).zfill(2)+':'+str(minutes).zfill(2)+':'+str(seconds).zfill(2)
            print(result)
Delta_Time()
