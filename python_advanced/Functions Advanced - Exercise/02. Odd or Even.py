def odd_even(odd_or_even, *args):
    odd_list = []
    even_list = []
    for el in args:
        if el % 2 == 0:
            even_list.append(el)
        else:
            odd_list.append(el)
    if odd_or_even == "Odd":
        return sum(odd_list) * len(args)
    else:
        return sum(even_list) * len(args)


command = input()
input_numbers = [int(x) for x in input().split()]

print(odd_even(command, *input_numbers))
