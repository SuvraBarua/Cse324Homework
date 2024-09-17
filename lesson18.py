matrix = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9]
]
print(matrix)
print(matrix[0])
print(matrix[0][2])
matrix[0][2] = 11
print(matrix)
for row in matrix:
	for item in row:
		print(item)
