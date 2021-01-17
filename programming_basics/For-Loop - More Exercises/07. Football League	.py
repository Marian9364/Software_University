capacity = int(input())
fans = int(input())
team1 = 0
team2 = 0
sector_a = 0
sector_b = 0
sector_v = 0
sector_g = 0
for fan in range(1, fans + 1):
    sector = input()
    if sector == "A":
        team1 += 1
        sector_a += 1
    elif sector == "B":
        team1 += 1
        sector_b += 1
    elif sector == "V":
        sector_v += 1
        team2 += 1
    elif sector == "G":
        sector_g += 1
        team2 += 1

percent_fans_in_a = sector_a / fans * 100
percent_fans_in_b = sector_b / fans * 100
percent_fans_in_v = sector_v / fans * 100
percent_fans_in_g = sector_g / fans * 100
all_fans_percent = fans / capacity * 100

print(f"{percent_fans_in_a:.2f}%")
print(f"{percent_fans_in_b:.2f}%")
print(f"{percent_fans_in_v:.2f}%")
print(f"{percent_fans_in_g:.2f}%")
print(f"{all_fans_percent:.2f}%")
