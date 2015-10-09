import argparse


class Query_Board:

	def SetCol(self, Col_Number, Value):
		for row in range(0, 256):
			self.board[row][Col_Number] = Value

	def SetRow(self, Row_Number, Value):
		for col in range(0, 256):
			self.board[Row_Number][col] = Value

	def QueryCol(self, Col_Number):
		Col_sum = 0
		for row in range(0, 256):
			Col_sum += self.board[row][Col_Number]
		return Col_sum

	def QueryRow(self, Row_Number):
		Row_sum = 0
		for col in range(0, 256):
			Row_sum += self.board[Row_Number][col]
		return Row_sum

	def __init__(self):
		self.board = [[0 for j in range(0, 256)] for i in range(0, 256)]


def Query_board_challenge():
	parser = argparse.ArgumentParser()
	parser.add_argument("filename")
	args = parser.parse_args()
	with open(args.filename) as f:
		qboard = Query_Board()
		for line in f:
			line = line.rstrip('\n')
			line = line.split(" ")

			if line[0] == 'SetCol':
				qboard.SetCol(int(line[1]), int(line[2]))

			if line[0] == 'SetRow':
				qboard.SetRow(int(line[1]), int(line[2]))

			if line[0] == 'QueryCol':
				val1 = qboard.QueryCol(int(line[1]))
				print(val1)
			if line[0] == 'QueryRow':
				val2 = qboard.QueryRow(int(line[1]))
				print(val2)
Query_board_challenge()