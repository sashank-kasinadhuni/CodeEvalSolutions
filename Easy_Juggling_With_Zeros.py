import argparse


def Juggling_Zeros():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    with open(args.filename) as f:
        for line in f:
            line = line.rstrip('\n')
            line = line.split()
            i = 0
            res = ""
            while(i != len(line)):
                flag = line[i]
                val = line[i + 1]
                i += 2
                if(flag == "00"):
                    res += "1" * len(val)
                else:
                    res += val
            print(int(res, 2))
Juggling_Zeros()
