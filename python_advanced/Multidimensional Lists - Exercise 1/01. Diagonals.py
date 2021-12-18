rows = int(input())
matrix = []
for _ in range(rows):
    line = [int(x) for x in input().split(", ")]
    matrix.append(line)

primary_diagonal = []
secondary_diagonal = []
matrix_index = 0
for i in range(rows):
    primary_diagonal.append(matrix[i][i])
for j in range(rows- 1, - 1, -1):

    current_number = matrix[matrix_index][j]
    secondary_diagonal.append(current_number)
    matrix_index += 1



print(f"Primary diagonal: {', '.join([str(x) for x in primary_diagonal])}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join([str(x) for x in secondary_diagonal])}. Sum: {sum(secondary_diagonal)}")
