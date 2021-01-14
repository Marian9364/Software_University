food = int(input())
food *= 1000
sum_food = 0
food_eaten = input()
while food_eaten != "Adopted":
    current_food = int(food_eaten)
    sum_food += current_food
    food_eaten = input()

leftovers = abs(sum_food - food)
if food < sum_food:
    print(f"Food is not enough. You need {leftovers} grams more.")
else:
    print(f"Food is enough! Leftovers: {leftovers} grams.")
