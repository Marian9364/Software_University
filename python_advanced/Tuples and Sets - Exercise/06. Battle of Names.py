n = int(input())
all_numbers = []
sum_of_name = 0
even_set = set()
odd_set = set()
for i in range(1, n + 1):
    name = input()
    for letter in name:
        sum_of_name += ord(letter)
    sum_of_name = sum_of_name // i
    all_numbers.append(sum_of_name)
    sum_of_name = 0

for num in all_numbers:
    if num % 2 == 1:
        odd_set.add(num)
    else:
        even_set.add(num)

sum_of_odd_set = sum(odd_set)
sum_of_even_set = sum(even_set)


if sum_of_odd_set == sum_of_even_set:
    new_set = odd_set.union(even_set)
    a = [str(x) for x in new_set]
    print(", ".join(a))
elif sum_of_odd_set > sum_of_even_set:
    difference = odd_set.difference(even_set)
    a = [str(x) for x in difference]
    print(", ".join(a))

elif sum_of_even_set > sum_of_odd_set:
    symmetric_different_values = odd_set.symmetric_difference(even_set)
    a = [str(x) for x in symmetric_different_values]
    print(", ".join(a))
