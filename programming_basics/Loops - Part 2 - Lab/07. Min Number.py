import sys
n = int(input())
min_num = sys.maxsize
while n > 0:
    num = int(input())
    if num < min_num:
        min_num = num

    n -= 1

print(min_num)
