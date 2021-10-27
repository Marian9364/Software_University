factor_and_count = int(input())
length = int(input())

my_list = []

for num in range(1,length + 1):
    new_number =  factor_and_count * num
    my_list.append(new_number)

print(my_list)
