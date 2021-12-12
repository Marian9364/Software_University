import sys
from collections import deque
from io import StringIO

test_string_1 = """20 62 99 35 0 150
120 60 10 1 70 10
+ - + + / * - - /
"""
test_string_2 = """30
15 9 5 150 8
* + + * -
"""
#sys.stdin = StringIO(test_string_1)
#sys.stdin = StringIO(test_string_2)

working_bees = deque([int(x) for x in input().split()])
nectar_stack = [int(x) for x in input().split()]
signs = deque(input().split())
honey = 0
signs_collection = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "/": lambda a, b: a / b,
    "*": lambda a, b: a * b,
}
while True:
    if not nectar_stack or not working_bees:
        break
    bee = working_bees.popleft()
    nectar = nectar_stack.pop()
    if nectar < bee:
        working_bees.appendleft(bee)
        continue
    else:
        if nectar <= 0:
            signs.popleft()
            continue
        honey += abs(signs_collection[signs.popleft()](bee, nectar))

print(f"Total honey made: {honey}")
if working_bees:
    print(f"Bees left: {', '.join([str(x) for x in working_bees])}")
if nectar_stack:
    print(f"Nectar left: {', '.join([str(x) for x in nectar_stack])}")



