numbers = input().split(", ")
integers = [int(el) for el in numbers]
boundary = 10
for i in range(max(integers)):
    if len(numbers) == 0:
        break
    result_list = []
    for num in numbers:
        num = int(num)
        if num <= boundary:
            result_list.append(num)
    for result in result_list:
        numbers.remove(str(result))

    print(f"Group of {boundary}'s: {result_list}")
    boundary += 10
