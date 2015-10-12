import argparse

def Word_To_Number():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    RefTable = {'zero':'0','one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
    with open(args.filename) as f:
        for line in f:
        	line = line.rstrip('\n')
        	line = line.split(';')
        	line[:] = [RefTable[i] for i in line]
        	print(''.join(line))

Word_To_Number()        	