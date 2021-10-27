single_string = input().split()
new_list = []
for num in single_string:
    if int(num) > 0:
        num = -1 * int(num)
    elif int(num) <= 0:
        num = abs(int((num)))
    new_list.append(num)

print(new_list)
