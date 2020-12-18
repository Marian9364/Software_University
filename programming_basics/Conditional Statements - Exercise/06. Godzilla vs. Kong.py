budget = float(input())
statists = int(input())
cloths_per_statist = float(input())

decor = budget * 0.1
statists_with_clothes = 0
if statists > 150:
    cloths_per_statist *= 0.9
    statists_with_clothes = cloths_per_statist * statists
else:
    statists_with_clothes = cloths_per_statist * statists

expences = decor + statists_with_clothes
diff = abs(expences - budget)
if expences > budget:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")
