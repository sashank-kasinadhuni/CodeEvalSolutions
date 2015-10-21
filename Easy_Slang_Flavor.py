import argparse


def Slang_Flavor():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    Base = [', yeah!', ', this is crazy, I tell ya.', ', can U believe this?',
            ', eh?',
            ', aw yea.',
            ', yo.',
            '? No way!',
            '. Awesome!']
    prev_op = 'dont_switch'
    idx = 0        
    with open(args.filename) as f:
        for line in f:
            line = line.rstrip('\n')

            result = ''
            for i in line :
            	if i == '?' or i=='.' or i =='!':
            		if prev_op == 'switch':
            			result += Base[idx%9]
            			idx+=1
            			prev_op = 'dont_switch'
            		else:
            			result+=i
            			prev_op = 'switch'
            	else:
            		result+= i
            print(result)
Slang_Flavor()           					
