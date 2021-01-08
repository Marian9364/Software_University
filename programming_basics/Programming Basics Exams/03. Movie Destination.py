budget = float(input())
destination = input()
season = input()
days = int(input())
price = 0

if destination == "Dubai":
    if season == "Winter":
        price = 45000
    elif season == "Summer":
        price = 40000
elif destination == "Sofia":
    if season == "Winter":
        price = 17000
    elif season == "Summer":
        price = 12500
elif destination == "London":
    if season == "Winter":
        price = 24000
    elif season == "Summer":
        price = 20250

final_price = price * days

if destination == "Dubai":
    final_price *= 0.7

if destination == "Sofia":
    final_price *= 1.25

diff = abs(budget - final_price)
if budget >= final_price:
    print(f"The budget for the movie is enough! We have {diff:.2f} leva left!")
else:
    print(f"The director needs {diff:.2f} leva more!")
