import sys
from io import StringIO
#test_string_1 = """"""
#test_string_2 = "r ue nge ora bl ed"
#sys.stdin = StringIO(test_string_1)
#sys.stdin = StringIO(test_string_2)

(rows, cols) = map(int, input().split())

matrix = []
for _ in range(rows):
    line = [x for x in input().split()]
    matrix.append(line)


while True:
    command = input()
    if command == "END":
        break
    data = command.split()
    if data[0] != "swap" or len(data) != 5:
        print("Invalid input!")
        continue
    else:
        row_1 = int(data[1])
        col_1 = int(data[2])
        row_2 = int(data[3])
        col_2 = int(data[4])
        if row_1 not in range(len(matrix)) or row_2 not in range(len(matrix)) \
            or col_1 not in range(len(matrix[0])) or col_2 not in range(len(matrix[0])):
            print("Invalid input!")
            continue
        elif row_1 < 0 or row_2 < 0 or col_1 < 0 or col_2 < 0:
            print("Invalid input!")
            continue

        else:
            matrix[row_1][col_1], matrix[row_2][col_2] = matrix[row_2][col_2], matrix[row_1][col_1]
            for row in matrix:
                print(' '.join([str(x) for x in row]))
