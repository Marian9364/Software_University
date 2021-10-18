num_of_commands = int(input())

stack = []
reversed_stack = []

for i in range(num_of_commands):
    token = input().split()
    command = int(token[0])
    if command == 1:
        stack.append(int(token[1]))
    if stack:
        if command == 2:
            stack.pop()
        elif command == 3:
            print(max(stack))
        elif command == 4:
            print(min(stack))

for i in range(len(stack)):
    reversed_stack.append(stack.pop())

reversed_stack = [str(x) for x in reversed_stack]
print(", ".join(reversed_stack))
