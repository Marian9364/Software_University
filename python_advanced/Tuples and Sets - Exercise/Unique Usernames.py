n = int(input())
l = []

for _ in range(n):
    name = input()
    l.append(name)

unique_list_of_names = set(l)

for unique_name in unique_list_of_names:
    print(unique_name)
