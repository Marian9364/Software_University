#program that is checking if a number is between 100 and 200

num = int(input())

if num < 100:
    print("Less than 100")
elif num <= 200:
    print("Between 100 and 200")
else:
    print("Greater than 200")
