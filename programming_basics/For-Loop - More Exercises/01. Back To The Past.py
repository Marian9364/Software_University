money_recieved = float(input())
year = int(input())
age = 18
for i in range(1800, year + 1):
    if i % 2 == 0:
        if i >= 1802:
            age +=1
        money_recieved-= 12000
    elif i % 2 == 1:
        age+= 1
        money_recieved-= 12000 + (50 * age)

if money_recieved < 0:
    money_needed = abs(money_recieved)
    print(f"He will need {money_needed:.2f} dollars to survive.")
else:

    print(f"Yes! He will live a carefree life and will have {money_recieved:.2f} dollars left.")
