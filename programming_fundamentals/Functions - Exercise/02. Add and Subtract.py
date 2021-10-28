def sum_numbers(int1, int2,):
    sum_ints = int1 + int2
    return sum_ints

def subtract(int1, int2, num3):
    subtracted_sum = None
    subtracted_sum = sum_numbers(int1, int2) - num3
    return subtracted_sum

def add_and_subtract(int1, int2, num3):
    sum_numbers(int1, int2)
    subtract(int1, int2, num3)

    final_sum = subtract(int1, int2, num3)
    return final_sum


print(add_and_subtract(int(input()), int(input()), int(input())))
