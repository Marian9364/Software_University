n, m = [int(x) for x in (input().split())]

list_1 = []
list_2 = []

for _ in range(n):
    num = int(input())
    list_1.append(num)

for _ in range(m):
    num = int(input())
    list_2.append(num)

set_1 = set(list_1)
set_2 = set(list_2)

for number in set_1.intersection(set_2):
    print(number)

