bottles = int(input())

bottle_in_ml = bottles * 750
dishes_counter = 0
pots_counter = 0
command = input()
counter = 0
while command != "End":
    counter += 1
    dishes = int(command)
    if counter % 3 == 0:
        pots_counter += dishes
        current_dish_in_ml = dishes * 15
    else:
        dishes_counter += dishes
        current_dish_in_ml = dishes * 5



    bottle_in_ml -= current_dish_in_ml
    if bottle_in_ml < 0:
        break

    command = input()

if command == "End":
    print(f"Detergent was enough!")
    print(f"{dishes_counter} dishes and {pots_counter} pots were washed.")
    print(f"Leftover detergent {abs(bottle_in_ml)} ml.")
else:
    print(f"Not enough detergent, {abs(bottle_in_ml)} ml. more necessary!")
