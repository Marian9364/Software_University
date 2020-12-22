#checking if the money are enough and printing out the difference

age = int(input())
washing_mashine_price = float(input())
toy_price = int(input())
toys_count = 0
money = 0
for i in range (1, age + 1):
    if i % 2 == 1:
        toys_count += 1
    elif i % 2 == 0:
        money += i * 5
        money -= 1

toys_money = toys_count * toy_price
final_money = money + toys_money
diff = abs(final_money - washing_mashine_price)
if final_money >= washing_mashine_price:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")

