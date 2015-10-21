import argparse


def RollerCoaster_Case():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    with open(args.filename) as f:
        for line in f:
            swapCase = "upper"
            line = line.rstrip('\n')
            #str_list = list(line)
            result = ""
            for i in range(0, len(line)):
                if(line[i].isalpha()):
                    if swapCase == "upper":
                        result += line[i].upper()
                        swapCase = "lower"
                    else:
                        result += line[i].lower()
                        swapCase = "upper"
                else:
                	result+= line[i]        
            print(result)
RollerCoaster_Case()
