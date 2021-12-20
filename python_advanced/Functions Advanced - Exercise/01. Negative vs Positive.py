def positive_or_negative_check(list_of_nums):
    positives = []
    negatives = []
    for number in list_of_nums:
        if number > 0:
            positives.append(number)
        else:
            negatives.append(number)
    print(sum(negatives))
    print(sum(positives))
    if abs(sum(negatives)) > sum(positives):
        return "The negatives are stronger than the positives"
    return "The positives are stronger than the negatives"


input_numbers = [int(x) for x in input().split()]
print(positive_or_negative_check(input_numbers))

          
