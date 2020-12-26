money_needed = float(input())
current_money = float(input())
days_spend = 0
days = 0
while days_spend < 5:
    days += 1
    command = input()
    money_input = float(input())
    if command == "spend":
        days_spend += 1
        current_money = current_money - money_input
        if current_money < 0:
            current_money = 0
    elif command == "save":
        days_spend = 0
        current_money += money_input
        if current_money >= money_needed:
            break




if current_money >= money_needed:
    print(f"You saved the money for {days} days. ")
else:
    print(f"You can't save the money.")
    print(days)

