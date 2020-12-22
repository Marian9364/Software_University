n = int(input())

max_num = -99999999
min_num = 99999999

for i in range( 0, n):
    number = int(input())
    if number > max_num:
        max_num = number
    if number < min_num:
        min_num = number
        
        
print(f"Max number: {max_num}")
print(f"Min number: {min_num}")
