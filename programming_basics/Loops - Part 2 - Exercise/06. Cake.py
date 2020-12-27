w = int(input())
l = int(input())

pieces = w * l

while pieces > 0:
    command = input()
    if command == "STOP":
        print(f"{pieces} pieces are left.")
        break
    else:
        taken_pieces = int(command)
        pieces -= taken_pieces
else:
    print(f"No more cake left! You need {abs(pieces)} pieces more.")
