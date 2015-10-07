import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    # print(args.filename)
    with open(args.filename) as f:
        for line in f:
            nextline = [int(x) for x in line.rstrip('\n').split()]
            output = [str(x) if(x % nextline[0] != 0 and x % nextline[1] != 0) else "FB" if(
                x % nextline[0] == 0 and x % nextline[1] == 0) else "F" if(x % nextline[0] == 0) else "B" for x in range(1,nextline[2]+1)]
            print(" ".join(output))


main()
