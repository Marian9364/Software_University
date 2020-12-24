import sys
n = int(input())
max_num = -sys.maxsize
while n > 0:
    num = int(input())
    if num > max_num:
        max_num = num
    
    n -= 1
    
print(max_num)
