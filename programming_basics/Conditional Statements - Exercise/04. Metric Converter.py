#metric converter (mm/cm/m)

num = float(input())
metrical_1 = input()
metrical_2 = input()
m = 0
cm = 0
mm = 0
if metrical_1 == "mm" and metrical_2 == "m":
    mm = num
    mm *= 0.001
    print(f"{mm:.3f}")
elif metrical_1 == "mm" and metrical_2 == "cm":
    mm = num
    mm *= 0.1
    print(f"{mm:.3f}")
elif metrical_1 == "cm" and metrical_2 == "mm":
    cm = num
    cm *= 10
    print(f"{cm:.3f}")
elif metrical_1 == "cm" and metrical_2 == "m":
    cm = num
    cm *= 0.01
    print(f"{cm:.3f}")
elif metrical_1 == "m" and metrical_2 == "mm":
    m = num
    m *= 1000
    print(f"{m:.3f}")
elif metrical_1 == "m" and metrical_2 == "cm":
    m = num
    m *= 100
    print(f"{m:.3f}")

