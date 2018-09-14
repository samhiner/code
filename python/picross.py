import math
#import matrix_print.py

###

board = [
	[[], [1], [1], [1], [1], []],
	[[], 0, 0, 0, 0, 0],
	[[4], 0, 0, 0, 0, 0],
	[[], 0, 0, 0, 0, 0],
	[[], 0, 0, 0, 0, 0], #, 0
	[[], 0, 0, 0, 0, 0]
]

###

width = len(board[0]) - 1
height = len(board) - 1

for x in board:
	#TODO make this read array of objects as well like x[0][y]
	if x[0] > width/2:
		if width % 2 == 0:
			pass
			#TODO add code for even sized boards
		else:
			mid_index = math.ceil(width/2)
			x[mid_index] = 1

#matrix_print.show(board)
print(board)