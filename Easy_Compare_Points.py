import argparse


def Compare_Points():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    Longtitude = {"S","here","N"}
    Latitude = {"W","here","E"}
    with open(args.filename) as f:
        for line in f:
            line = line.rstrip('\n')
            line = [int(i) for i in line.split()]
            start = (line[0],line[1])
            end = (line[2],line[3])
            lat = "W" if start[0]>end[0] else "E" if start[0]<end[0] else ""
            lon = "S" if start[1]>end[1] else "N" if start[1]<end[1] else ""
            res = lon+lat
            if(res == ""):
            	res = "here"
            print(res)
Compare_Points()            