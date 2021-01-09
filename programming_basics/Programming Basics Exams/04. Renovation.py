import math
wall_height = int(input())
wall_width = int(input())
percent_not_to_be_painted = int(input())
all_walls = wall_height * wall_width * 4
to_be_painted = math.ceil(all_walls - (all_walls / 100 * percent_not_to_be_painted))
command = int(input())
while command != "Tired!":
    liters = int(command)
    to_be_painted -= liters
    if to_be_painted <= 0:
        break
    command = input()




if to_be_painted < 0:
    print(f"All walls are painted and you have {abs(to_be_painted)} l paint left!")
elif to_be_painted == 0:
    print("All walls are painted! Great job, Pesho!")

else:
    print(f"{to_be_painted} quadratic m left.")



