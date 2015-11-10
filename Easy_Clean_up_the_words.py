import argparse


def Clean_up_the_words():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    with open(args.filename) as f:
        for line in f:
            line = line.rstrip("\n")
            curr = list()
            res = list()
            for i in line:
                if (ord(i) >= 97 and ord(i) <= 122) or (ord(i) >= 65 and ord(i) <= 90):
                    curr.append(i.lower())
                else:
                    if len(curr)!=0:
                    	res.append("".join(curr))
                    	curr[:] =[]
            print(" ".join(res))
Clean_up_the_words()
