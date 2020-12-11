#printing out if an animal is an mammal, reptile or unknown

animal = input()

if animal == "dog":
    print("mammal")
elif animal == "snake" or animal == "tortoise" or animal == "crocodile":
    print("reptile")
else:
    print("unknown")
