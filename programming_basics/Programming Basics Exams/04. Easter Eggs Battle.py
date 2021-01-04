first_player = int(input())
second_player = int(input())
command = input()

while command != "End of battle" and first_player != 0 and second_player != 0:
    commands = command
    if commands == "one":
        second_player -= 1
    elif commands == "two":
        first_player -= 1
    if first_player == 0:
        break
    elif second_player == 0:
        break
    command = input()
if first_player == 0:
    print (f"Player one is out of eggs. Player two has {second_player} eggs left.")
if second_player == 0:
    print(f"Player two is out of eggs. Player one has {first_player} eggs left.")
if first_player != 0 and second_player != 0:
    print(f"Player one has {first_player} eggs left.")
    print(f"Player two has {second_player} eggs left.")
