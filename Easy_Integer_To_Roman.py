import argparse
from bisect import bisect_left

def binary_search(a, x, lo=0, hi=None):   # can't use a to specify default for hi
    hi = hi if hi is not None else len(a) # hi defaults to len(a)   
    pos = bisect_left(a,x,lo,hi)          # find insertion position
    return (pos if pos != hi and a[pos] == x else -1) # don't walk off the end

def Integer_To_Roman():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    BaseList = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    Lookup = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50:
              "L", 90: "XC", 100: "C", 400: "CD", 500: "D", 900: "CM", 1000: "M"}
    with open(args.filename) as f:
        for line in f:
            line = line.rstrip('\n')
            val = int(line)
            result = ""
            while(val != 0):
                print("val: ",val)
                idx = binary_search(BaseList, val,0 ,len(BaseList))
                val -= BaseList[idx]
                next_Roman = Lookup[BaseList[idx]]
                result += next_Roman
            print(result)
Integer_To_Roman()
