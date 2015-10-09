import argparse
from collections import Counter

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

def is_Desc(number):
	digits = get_Digits(int(number))
	#print("Digits : ",digits)
	counts = Counter(digits)
	#print("Counts : ",counts)
	for i in range(0,len(digits)):
		if (digits[i] != counts[i]):
			return (0)
	return(1)		

def Self_Describing():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    with open(args.filename) as f:
        for line in f:
        	line= line.rstrip('\n')
        	print(is_Desc(line))

Self_Describing()        	