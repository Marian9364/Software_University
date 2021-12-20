def even_odd(*args):
    list_of_numbers = list(args[:-1])
    command = args[-1]
    even_list = []
    odd_list = []

    for el in list_of_numbers:
        if int(el) % 2 == 0:
            even_list.append(int(el))
        else:
            odd_list.append(int(el))
    if command == "even":
        return even_list
    else:
        return odd_list
