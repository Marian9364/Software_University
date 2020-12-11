#program calculating the trade commission of a trade in a specific town

town = input()
sells = float(input())
commission = 0
if town == "Sofia":
    if sells >= 0 and sells <= 500:
        commission = sells * 0.05
    elif sells >= 500 and sells <= 1000:
        commission = sells * 0.07
    elif sells > 1000 and sells <= 10000:
        commission = sells * 0.08
    elif sells > 10000:
        commission = sells * 0.12
elif town == "Varna":
    if sells >= 0 and sells <= 500:
        commission = sells * 0.045
    elif sells >= 500 and sells <= 1000:
        commission = sells * 0.075
    elif sells > 1000 and sells <= 10000:
        commission = sells * 0.1
    elif sells > 10000:
        commission = sells * 0.13
elif town == "Plovdiv":
    if sells >= 0 and sells <= 500:
        commission = sells * 0.055
    elif sells >= 500 and sells <= 1000:
        commission = sells * 0.08
    elif sells > 1000 and sells <= 10000:
        commission = sells * 0.12
    elif sells > 10000:
        commission = sells * 0.145

if commission > 0:
    print(f"{commission:.2f}")
else:
    print("error")
