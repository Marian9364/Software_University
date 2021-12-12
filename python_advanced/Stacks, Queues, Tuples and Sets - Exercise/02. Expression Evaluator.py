from collections import deque

expression = input().split()

numbers = deque()

arithmetic_expressions = {
    "+": lambda a, b : a + b,
    "-": lambda a, b: a - b,
    "*": lambda  a, b: a * b,
    "/": lambda a, b: a // b,
}

for char in expression:
    if char in arithmetic_expressions:
        num_1 = numbers.popleft()
        while numbers:
            num_2 = numbers.popleft()
            num_1 = arithmetic_expressions[char](num_1, num_2)
        numbers.append(num_1)
    else:
        numbers.append(int(char))

print(numbers.popleft())

