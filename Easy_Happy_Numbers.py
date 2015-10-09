import argparse


def get_Digits_Squared(number):
	digits = list()
	if(number<10):
		digits.append(number**2)
		return digits
	while(number>=10):
		val = number%10
		digits.append(val**2)
		number //=10
	digits.append(number**2)	
	return digits


def is_Happy(number):
	path = list()
	path.append(number)
	while number != 1 :
		digits = get_Digits_Squared(number)
		#print(digits)
		number = sum(digits)
		if number in path:
			return 0
		else:
			path.append(number)
			#print(number, end='->')
		#print(number,end="->")	
	return 1


def Happy_Numbers():
	parser = argparse.ArgumentParser()
	parser.add_argument("filename")
	args = parser.parse_args()
	with open(args.filename) as f:
		for line in f:
			line = line.rstrip('\n')
			print(is_Happy(int(line)))
Happy_Numbers()