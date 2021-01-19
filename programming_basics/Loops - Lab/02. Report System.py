charity_amount = int(input())

sum_money_CS = 0
sum_money_CC = 0
sum_money = 0
count_transaction = 0
count_transaction_CC = 0
count_transaction_CS = 0

while charity_amount > sum_money:
    price_items = input()
    count_transaction += 1
    if price_items == "End":
        print("Failed to collect required money for charity.")
        break
    else:
        price_items = int(price_items)

    if count_transaction % 2 == 0:
        if price_items < 10:
            print("Error in transaction!")
        else:
            print("Product sold!")
            sum_money += int(price_items)
            sum_money_CC += int(price_items)
            count_transaction_CC += 1
    else:
        if price_items > 100:
            print("Error in transaction!")
        else:
            print("Product sold!")
            sum_money += int(price_items)
            sum_money_CS += int(price_items)
            count_transaction_CS += 1

if sum_money >= charity_amount:
    print(f"Average CS: {sum_money_CS / count_transaction_CS:.2f}")
    print(f"Average CC: {sum_money_CC / count_transaction_CC:.2f}")
