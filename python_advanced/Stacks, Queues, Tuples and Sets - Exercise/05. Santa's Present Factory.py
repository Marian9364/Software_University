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


materials_for_crafting = [int(x) for x in input().split()]
magic_level = deque([int(x) for x in input().split()])

presents_goal_dict = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle",
}
crafted_gifts = {}
task_done = False
while materials_for_crafting and magic_level:
    current_material = materials_for_crafting.pop()
    current_magic = magic_level.popleft()
    multiplication = current_material * current_magic
    if current_material == 0 and current_magic == 0:
        continue
    if current_material == 0:
        magic_level.appendleft(current_magic)
        continue
    if current_magic == 0:
        materials_for_crafting.append(current_material)
        continue

    if multiplication in presents_goal_dict:
        gift = presents_goal_dict[multiplication]
        if gift not in crafted_gifts:
            crafted_gifts[gift] = 1
        else:
            crafted_gifts[gift] += 1
    elif multiplication < 0:
        summ = current_material + current_magic
        materials_for_crafting.append(summ)
    elif multiplication > 0:
        materials_for_crafting.append(current_material + 15)


if ("Teddy bear" in crafted_gifts and "Bicycle" in crafted_gifts) or ("Doll" in crafted_gifts and "Wooden train" in crafted_gifts) :
    task_done = True


if task_done:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials_for_crafting:
    print(f"Materials left: {', '.join(reversed([str(x) for x in materials_for_crafting]))}")
if magic_level:
    print(f"Magic left: {', '.join([str(x) for x in magic_level])}")

for key, value in sorted(crafted_gifts.items()):
    print(f"{key}: {value}")

