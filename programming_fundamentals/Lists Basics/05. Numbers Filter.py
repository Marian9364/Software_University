n = int(input())

even = []
odd = []
negative = []
positive = []

for i in range(n):
    nums = int(input())
    if nums % 2 == 0:
        even.append(nums)
    if nums % 2 == 1:
        odd.append(nums)
    if nums >= 0:
        positive.append(nums)
    if nums < 0:
        negative.append(nums)
command = input()
if command == "even":
    print(even)
elif command == "odd":
    print(odd)
elif command == "negative":
    print(negative)
elif command == "positive":
    print(positive)
