eggs_count = int(input())

orange_counter = 0
blue_counter = 0
green_counter = 0
red_counter = 0
highest_num = -99999
for i in range (eggs_count):
    egg_color = input()
    if egg_color == "orange":
        orange_counter += 1
        if orange_counter > highest_num:
            highest_num = orange_counter
    elif egg_color == "blue":
        blue_counter += 1
        if blue_counter > highest_num:
            highest_num = blue_counter
    elif egg_color == "red":
        red_counter += 1
        if red_counter > highest_num:
            highest_num = red_counter
    elif egg_color == "green":
        green_counter += 1
        if green_counter > highest_num:
            highest_num = green_counter
max_eggs = max(red_counter, orange_counter, blue_counter, green_counter)


if highest_num == red_counter:
    highest_num = "red"
elif highest_num == orange_counter:
    highest_num = "orange"
elif highest_num == blue_counter:
    highest_num = "blue"
elif highest_num == green_counter:
    highest_num = "green"

print(f"Red eggs: {red_counter}")
print(f"Orange eggs: {orange_counter}")
print(f"Blue eggs: {blue_counter}")
print(f"Green eggs: {green_counter}")
print(f"Max eggs: {max_eggs} -> {highest_num}")
