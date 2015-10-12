import argparse

def Get_Codes(Code):
	Morse = {'.-':"A","-...":"B",'-.-.':"C",'-..':"D",'.':"E",'..-.':"F",'--.':"G",'....':"H",'..':"I",'.---':"J",'-.-':"K",'.-..':"L",'--':"M",'-.':"N",'---':"O",'.--.':"P",'--.-':"Q",'.-.':"R",'...':"S",'-':"T",'..-':"U",'...-':"V",'.--':"W",'-..-':"X",'-.--':"Y",'--..':"Z",'.----':"1",'..---':"2",'...--':"3",'....-':"4",'.....':"5",'-....':"6",'--...':"7","---..":"8",'----.':"9",'-----':"0"}
	partial_Code =''
	result = list()
	space = False
	for i in range(0,len(Code)):
		if Code[i] != ' ':
			partial_Code += Code[i]
		else:
			# print(partial_Code)
			if Code[i-1] == ' ':
				result.append(' ')
			else:
				result.append(Morse[partial_Code])
				partial_Code = ''	
	result.append(Morse[partial_Code])
	return result			


def Morse_Decoder():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    with open(args.filename) as f:
    	for line in f:
    		line = line.rstrip('\n')
    		# print("line",line)
    		result = Get_Codes(line)
    		# print(result)
    		print("".join(result))
Morse_Decoder()
