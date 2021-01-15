import math
cakes_count = int(input())
biggest_flour_num = -9999
biggest_sugar_num = -9999
sugar_sum = 0
flour_sum = 0
for i in range (1, cakes_count + 1):
    sugar = int(input())
    flour = int(input())
    sugar_sum += sugar
    flour_sum += flour
    if sugar > biggest_sugar_num:
        biggest_sugar_num = sugar
    if flour > biggest_flour_num:
        biggest_flour_num = flour
    i +=1



sugar_packs = sugar_sum / 950
flour_packs = flour_sum / 750
sugar_packs_final = math.ceil(sugar_packs)
flour_packs_final = math.ceil(flour_packs)


print(f"Sugar: {sugar_packs_final}")
print(f"Flour: {flour_packs_final}")
print(f"Max used flour is {biggest_flour_num} grams, max used sugar is {biggest_sugar_num} grams.")
