budget = float(input())
liters_fuel_needed = float(input())
day_of_week = input()

fuel_price = liters_fuel_needed * 2.10
guide = 100
expenses = fuel_price + guide
if day_of_week == "Sunday":
    expenses *= 0.8
elif day_of_week == "Saturday":
    expenses *= 0.9
diff = abs(budget - expenses)
if budget >= expenses:
    print(f"Safari time! Money left: {diff:.2f} lv. ")
else:
    print(f"Not enough money! Money needed: {diff:.2f} lv.")



