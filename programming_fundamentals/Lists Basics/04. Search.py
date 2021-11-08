n = int(input())
full_list = []
reworked_list = []
word = input()
for i in range(n):
    strings = input()
    full_list.append(strings)
for chars in full_list:
    if word in chars:
        reworked_list.append(chars)

print(full_list)
print(reworked_list)
