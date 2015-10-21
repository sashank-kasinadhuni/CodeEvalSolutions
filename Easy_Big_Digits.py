import argparse


def Big_Digits():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    Numbers = {'0': ['-**-', '*--*', '*--*', '*--*', '-**-'],
               '1': ['--*-', '-**-', '--*-', '--*-', '-***'],
               '2': ['***-', '---*', '-**-', '*---', '****'],
               '3': ['***-', '---*', '-**-', '---*', '***-'],
               '4': ['-*--', '*--*', '****', '---*', '---*'],
               '6': ['-**-', '*---', '***-', '*--*', '-**-'],
               '5': ['****', '*---', '***-', '---*', '***-'],
               '7': ['****', '---*', '--*-', '-*--', '-*--'],
               '8': ['-**-', '*--*', '-**-', '*--*', '-**-'],
               '9': ['-**-', '*--*', '-***', '---*', '-**-']}
    with open(args.filename) as f:
        for line in f:
            number = list(line)
            length = 0
            for i in range(0, 5):
                result = ""
                for k in number:
                    if k in Numbers:
                        result += Numbers[k][i]
                        result += '-'
                print(result)
                length = len(result)
            print('-' * length)
Big_Digits()
