from datetime import time
import argparse


def Scheduler():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    with open(args.filename) as f:
        for line in f:
            line = line.rstrip('\n')
            if(line == ""):
                continue
            timestamps = [time(int(x.split(':')[0]), int(x.split(':')[1]), int(
                x.split(':')[2])) for x in line.split(' ')]
            timestamps.sort(reverse=True)
            timestamps[:] = [str(x) for x in timestamps]
            print(" ".join(timestamps))

Scheduler()
