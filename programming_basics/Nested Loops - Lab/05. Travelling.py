destination = input()
money_saved = 0

while destination != "End":
    money_to_be_saved = float(input())
    while money_saved < money_to_be_saved:
        current_money = float(input())
        money_saved += current_money
        if money_saved >= money_to_be_saved:
            print(f"Going to {destination}!")
            money_saved = 0
            break
    destination = input()
