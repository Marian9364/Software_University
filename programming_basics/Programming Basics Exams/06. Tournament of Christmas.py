tournaments_count = int(input())
money_per_day = 0
money_won = 0
wins = 0
loses = 0
won_day = 0
lost_day = 0

for day in range(1, tournaments_count + 1):
    sport_type = input()
    while sport_type != "Finish":
        sport_input = sport_type
        result = input()
        if result == "win":
            money_per_day += 20
            money_won += 20
            wins += 1
        elif result == "lose":
            loses +=1
        sport_type = input()

    if wins > loses:
        won_day += 1
        money_won = money_won + (money_per_day * 0.1)
    else:
        lost_day += 1
    wins = 0
    loses = 0
    day += 1
    money_per_day = 0
bonus = 0.1 * won_day
money_won = money_won + (money_per_day * bonus)

if won_day > lost_day:

    money_won = money_won + (money_won * 0.20)
    print (f"You won the tournament! Total raised money: {money_won:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {money_won:.2f}")

