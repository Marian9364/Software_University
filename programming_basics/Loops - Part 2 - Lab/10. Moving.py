w = int(input())
l = int(input())
h = int(input())
free_space = w * l * h


command = input()

while command != "Done":
    current_command = int(command)
    free_space -= current_command
    if free_space <= 0:
        break
    command = input()

if free_space <= 0:
    space = abs(free_space)
    print(f"No more free space! You need {space} Cubic meters more.")
else:
    print(f"{free_space} Cubic meters left.")
