command = input()
database = {}
while command != "stop":
    resource = command
    amount = int(input())
    if resource not in database:
        database[resource] = amount
    else:
        database[resource] += amount

    command = input()

for key, value in database.items():
    print(f"{key} -> {value}")
