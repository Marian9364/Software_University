(rows, cols) = map(int, input().split())

matrix = []
for _ in range(rows):
    line = [x for x in input().split()]
    matrix.append(line)
square = 0
for r in range(rows - 1):
    for c in range (cols - 1):
        first_el = matrix[r][c]
        second_el = matrix[r][c+1]
        third_el = matrix[r+1][c]
        forth_el = matrix[r+1][c+1]
        if first_el == second_el and first_el == third_el and first_el == forth_el:
            square += 1
print(square)
