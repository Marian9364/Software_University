from itertools import permutations

def possible_permutations(numbers):
    permutations_list = permutations(numbers)
    for permutation in permutations_list:
        yield [x for x in permutation]



[print(n) for n in possible_permutations([1, 2, 3])]
