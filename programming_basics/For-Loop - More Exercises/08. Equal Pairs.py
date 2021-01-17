n = int(input())
sum_1 = 0
sum_2 = 0
max_diff = -999999
current_diff = 0

for i in range(n):
    a = int(input())
    b = int(input())
    current_sum = a + b
    if i % 2 == 0:
        sum_1 = current_sum
    else:
        sum_2 = current_sum

    if i >= 1:
        current_diff = abs(sum_1 - sum_2)
        if current_diff >= max_diff:
            max_diff = current_diff
    if  sum_1 == current_sum and sum_2 == 0:
        max_diff = 0


if max_diff == 0:
    print(f"Yes, value={current_sum}")
else:
    print(f"No, maxdiff={max_diff}")






