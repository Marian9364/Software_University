from collections import deque

parentheses = input()
opening_brackets = deque()
is_balanced = True
for el in parentheses:
    if el in "{[(":
        opening_brackets.append(el)
    else:
        if len(opening_brackets) == 0:
            is_balanced = False
            break
        last_op_bracket = opening_brackets.pop()
        pair = f"{last_op_bracket}{el}"
        if pair not in "(){}[]":
            is_balanced = False
            break


if is_balanced and len(opening_brackets) == 0:
    print("YES")
else:
    print("NO")
