days = int(input())
food = float(input())
sum_together = 0
cats_sum = 0
dogs_sum = 0
biscuits = 0
for i in range(1, days + 1):
    dog_food = int(input())
    cat_food = int(input())
    dogs_sum += dog_food
    cats_sum += cat_food
    if i % 3 == 0:
        current_biscuits = (dog_food + cat_food) * 0.1
        biscuits += current_biscuits
    sum_together = dogs_sum + cats_sum


food_eaten = (sum_together * 100) / food
dog_food_eaten = (dogs_sum * 100) / sum_together
cat_food_eaten = (cats_sum * 100) / sum_together


print(f"Total eaten biscuits: {round(biscuits)}gr.")
print(f"{food_eaten:.2f}% of the food has been eaten.")
print(f"{dog_food_eaten:.2f}% eaten from the dog.")
print(f"{cat_food_eaten:.2f}% eaten from the cat.")
