import argparse

def get_Digits(number):
	digits = list()
	if(number<10):
		digits.append(number)
		return digits
	while(number>=10):
		val = number%10
		digits.append(val)
		number //=10
	digits.append(number)	
	return digits[::-1]

def Armstrong_Numbers():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    with open(args.filename) as f:
        for line in f:
        	line = line.rstrip('\n')
        	digits = get_Digits(int(line))
        	number = sum([i**len(digits) for i in digits])
        	if(number == int(line)):
        		print(True)
        	else:
        		print(False)
Armstrong_Numbers()        			