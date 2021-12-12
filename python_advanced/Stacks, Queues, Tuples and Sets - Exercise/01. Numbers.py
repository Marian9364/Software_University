import sys
from io import StringIO

test_string_1 = """1 2 3 4 5
1 2 3
3
Add First 5 6
Remove Second 8 9 11
Check Subset
"""
test_string_2 = """5 4 2 9 9 5 4
1 1 1 5 6 5
4
Add First 5 6 9 3
Add Second 1 2 3 3 3
Check Subset
Remove Second 1 2 3 4 5
"""
#sys.stdin = StringIO(test_string_1)
#sys.stdin = StringIO(test_string_2)

first_set = set([int(x) for x in input().split()])
second_set = set([int(x) for x in input().split()])


n = int(input())

for _ in range(n):
    command = input().split()
    to_do = command[0]
    if to_do == "Add":
        numbers_to_add = command[2:]
        if command[1] == "First":
            for num in numbers_to_add:
                first_set.add(int(num))
        elif command[1] == "Second":
            for num in numbers_to_add:
                second_set.add(int(num))
    elif to_do == "Remove":
        numbers_to_remove = command[2:]
        numbers_to_remove = [int(x) for x in numbers_to_remove]
        if command[1] == "First":
            for num in numbers_to_remove:
                if num in first_set:
                    first_set.remove(num)
        elif command[1] == "Second":
            for num in numbers_to_remove:
                if num in second_set:
                    second_set.remove(num)
    else:
        if first_set.issubset(second_set):
            print("True")
        elif second_set.issubset(first_set):
            print("True")
        else:
            print("False")

#[print(", ".join(str(x))) for x in sorted(first_set)]
first_set = sorted(first_set)
second_set = sorted(second_set)
string_first = [str(x) for x in first_set]
string_second = [str(x) for x in second_set]

print(", ".join(string_first))
print(", ".join(string_second))
