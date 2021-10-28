def odd_even_sum(n):

    odd_sum = 0
    even_sum = 0
    for i in n:
        if int(i) % 2 == 1:
            odd_sum += int(i)
        elif int(i) % 2 == 0:
            even_sum += int(i)

    print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")
num = input()
odd_even_sum(num)
