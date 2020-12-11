#printing out the final price of a product * quantity in a week day

fruit = input()
day_of_week = input()
quantity = float(input())
price = 0
is_weekday = day_of_week == "Monday" or day_of_week == "Tuesday" or day_of_week == "Wednesday" or \
    day_of_week == "Thursday" or day_of_week == "Friday"
is_weekend = day_of_week == "Saturday" or day_of_week == "Sunday"
if is_weekday:
    if fruit == "banana":
        price = 2.50
    elif fruit == "apple":
        price = 1.20
    elif fruit == "orange":
        price = 0.85
    elif fruit == "grapefruit":
        price = 1.45
    elif fruit == "kiwi":
        price = 2.70
    elif fruit == "pineapple":
        price = 5.50
    elif fruit == "grapes":
        price = 3.85


elif is_weekend:
    if fruit == "banana":
        price = 2.70
    elif fruit == "apple":
        price = 1.25
    elif fruit == "orange":
        price = 0.9
    elif fruit == "grapefruit":
        price = 1.60
    elif fruit == "kiwi":
        price = 3
    elif fruit == "pineapple":
        price = 5.60
    elif fruit == "grapes":
        price = 4.20

final_price = price * quantity
if final_price > 0:
    print(f"{final_price:.2f}")
else:
    print("error")
