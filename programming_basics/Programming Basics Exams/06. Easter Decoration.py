clients_count = int(input())
summ = 0
items = 0
summ_all = 0
average_bill = 0
for i in range(clients_count):
    first_grocery = input()
    while first_grocery != "Finish":
        grocery = first_grocery
        if grocery == "basket":
            summ += 1.50
            items += 1
        elif grocery == "wreath":
            summ += 3.80
            items += 1
        elif grocery == "chocolate bunny":
            summ += 7
            items += 1
        first_grocery = input()

    if items % 2 == 0:
        summ *= 0.8
    print(f"You purchased {items} items for {summ:.2f} leva.")
    summ_all += summ
    average_bill = summ_all / clients_count
    summ = 0
    items = 0


print(f"Average bill per client is: {average_bill:.2f} leva.")
