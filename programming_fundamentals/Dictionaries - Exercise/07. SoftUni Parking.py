n = int(input())
registry = {}
for _ in range(n):
    command = input().split()
    reg_or_unregister = command[0]
    name = command[1]
    if reg_or_unregister == "register":
        plate_number = command[2]
        if name not in registry:
            registry[name] = plate_number
            print(f"{name} registered {plate_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {plate_number}")
    elif reg_or_unregister == "unregister":
        if name not in registry:
            print(f"ERROR: user {name} not found")
        else:
            print(f"{name} unregistered successfully")
            registry.__delitem__(name)

for username, plate in registry.items():
    print(f"{username} => {plate}")
