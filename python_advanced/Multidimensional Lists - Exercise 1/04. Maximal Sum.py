import sys

(rows, cols) = map(int, input().split())

biggest_sum = -sys.maxsize
matrix = []
for _ in range(rows):
    line = [int(x) for x in input().split()]
    matrix.append(line)

best_row = 0
best_col = 0

for r in range(rows - 2):
    for c in range (cols - 2):
        first_el = matrix[r][c]
        second_el = matrix[r][c+1]
        third_el = matrix[r][c+2]
        forth_el = matrix[r+1][c]
        fifth_el = matrix[r+1][c+1]
        sixth_el = matrix[r+1][c+2]
        seventh_el = matrix[r+2][c]
        eight_el = matrix[r+2][c+1]
        ninth_el = matrix[r+2][c+2]

        current_sum = first_el + second_el + third_el + forth_el \
                      + fifth_el + sixth_el + seventh_el + eight_el + ninth_el
        if current_sum > biggest_sum:
            biggest_sum = current_sum
            best_row = r
            best_col = c

print(f"Sum = {biggest_sum}")
print(matrix[best_row][best_col],matrix[best_row][best_col+1],matrix[best_row][best_col+2])
print(matrix[best_row+1][best_col],matrix[best_row+1][best_col+1],matrix[best_row+1][best_col+2])
print(matrix[best_row+2][best_col],matrix[best_row+2][best_col+1],matrix[best_row+2][best_col+2])
