import argparse


def Trick_or_treat():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    with open(args.filename) as f:
        for line in f:
            line = line.rstrip('\n')
            line = line.split(',')
            line[:] = [i.split(':') for i in line]
            counts =  dict()
            for i in line:
                counts[i[0].lstrip(' ')] = int(i[1])
            result = ((counts['Vampires']*3 + counts['Zombies']*4 + counts['Witches']*5) * counts['Houses'])//(counts['Vampires'] + counts['Zombies'] + counts['Witches'] )
            print(result)
                    
Trick_or_treat()            