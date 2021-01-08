wanted_win = float(input())
is_accomplished = False
summ = 0
while summ < wanted_win:
    cocktail = input()
    if cocktail == "Party!":
        break
    cocktails_count = int(input())
    cocktail_price = len(cocktail)
    cocktails_price = cocktails_count * cocktail_price
    if cocktails_price % 2 == 1:
        cocktails_price *= 0.75
    summ += cocktails_price
    #if summ >= wanted_win or cocktail == "Party!" or cocktails_count == str("Party!"):
        #is_accomplished = True
        #break

if summ >= wanted_win:
    print(f"Target acquired.")
    print(f"Club income - {summ:.2f} leva.")
else:
    diff = abs(summ - wanted_win)
    print(f"We need {diff:.2f} leva more.")
    print(f"Club income - {summ:.2f} leva.")

