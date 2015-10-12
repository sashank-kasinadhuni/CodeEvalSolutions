import argparse


def find_Roman(number):
    Numerals = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50:
                "L", 90: "XC", 100: "C", 400: "CD", 500: "D", 900: "CM", 1000: "M"}
    Base = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    result = ""
    while(number != 0):
        prevVal = 0
        for i in Base:
            if(number > Base[-1]):
                number -= Base[-1]
                result += Numerals[Base[-1]]
                break
            if i < number:
                prevVal = i
            elif i == number:
                number -= i
                result += Numerals[i]
                break
            else:
                #print("PrevVal: {} ,Number {}".format(prevVal, number))
                number -= prevVal
                result += Numerals[prevVal]
                break
    return result


def Integer_To_Roman():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    with open(args.filename) as f:
        for line in f:
            line = line.rstrip('\n')
            #print("Last Number: ", int(line))
            print(find_Roman(int(line)))
Integer_To_Roman()
