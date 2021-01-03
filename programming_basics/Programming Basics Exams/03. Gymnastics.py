country = input()
device = input()

if device == "ribbon":
    if country == "Russia":
        difficulty = 9.100
        performance = 9.400
    elif country == "Bulgaria":
        difficulty = 9.600
        performance = 9.400
    elif country == "Italy":
        difficulty = 9.200
        performance = 9.500
elif device == "hoop":
    if country == "Russia":
        difficulty = 9.300
        performance = 9.800
    elif country == "Bulgaria":
        difficulty = 9.550
        performance = 9.750
    elif country == "Italy":
        difficulty = 9.450
        performance = 9.150
elif device == "rope":
    if country == "Russia":
        difficulty = 9.600
        performance = 9.000
    elif country == "Bulgaria":
        difficulty = 9.500
        performance = 9.400
    elif country == "Italy":
        difficulty = 9.700
        performance = 9.150


score = difficulty + performance

not_enough = 20 - score

percent_not_enough = (not_enough/20) * 100

print(f"The team of {country} get {score:.3f} on {device}.")
print(f"{percent_not_enough:.2f}%")
