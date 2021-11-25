input_string = input()
tuple_to_fill = {}

for el in input_string:
    if el not in tuple_to_fill:
        tuple_to_fill[el] = 1
    else:
        tuple_to_fill[el] += 1

for key, value in sorted(tuple_to_fill.items(), key=lambda x: x[0]):
    print(f"{key}: {value} time/s")

