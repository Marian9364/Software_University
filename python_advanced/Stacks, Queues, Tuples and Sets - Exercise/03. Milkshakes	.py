import sys
from collections import deque
from io import StringIO

test_string_1 = """20, 24, -5, 17, 22, 60, 26
26, 60, 22, 17, 24, 10, 55

"""
test_string_2 = """-10, -2, -30, 10
-5

"""
#sys.stdin = StringIO(test_string_1)
#sys.stdin = StringIO(test_string_2)

chocolate = [int(x) for x in input().split(", ")]
milk_cups = deque(int(x) for x in input().split(", "))

milkshakes = 0

while chocolate and milk_cups and milkshakes < 5:
    choc = chocolate.pop()
    cup = milk_cups.popleft()
    if choc <= 0 and cup <= 0:
        continue
    if choc <= 0:
        milk_cups.appendleft(cup)
        continue
    if cup <= 0:
        chocolate.append(choc)
        continue

    if choc == cup:
        milkshakes += 1
    else:
        milk_cups.append(cup)
        chocolate[-1] -= 5

if milkshakes < 5:
    print("Not enough milkshakes.")
else:
    print("Great! You made all the chocolate milkshakes needed!")

if chocolate:
    print(f"Chocolate: {', '.join([str(x) for x in chocolate])}")
else:
    print("Chocolate: empty")

if milk_cups:
    print(f"Milk: {', '.join([str(x) for x in milk_cups])}")
else:
    print("Milk: empty")







