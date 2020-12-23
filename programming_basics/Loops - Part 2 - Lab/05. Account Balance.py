deposits = int(input())

counter = 1
summ = 0
while deposits >= counter:
    deposit = float(input())
    if deposit < 0:
        print("Invalid operation!")
        break
    else:
        print(f"Increase: {deposit:.2f}")
        summ += deposit
    counter += 1


print(f"Total: {summ:.2f}")
