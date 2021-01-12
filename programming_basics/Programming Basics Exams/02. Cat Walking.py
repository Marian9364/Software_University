walk_in_min = int(input())
times_walked = int(input())
calories_taken = int(input())

walk = walk_in_min * times_walked
calories_burned = walk * 5

half_the_cal = calories_taken / 2

if calories_burned >= half_the_cal:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {calories_burned}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {calories_burned}.")
