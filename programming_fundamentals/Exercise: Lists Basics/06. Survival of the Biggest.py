list_of_ints = input().split()
n = int(input())
#print(list_of_ints)
new_int_list = []
for i in list_of_ints:
    new_int_list.append(int(i))
#print(new_int_list)
for i in range(n):

    b = min(new_int_list)
    new_int_list.remove(b)


print(new_int_list)
