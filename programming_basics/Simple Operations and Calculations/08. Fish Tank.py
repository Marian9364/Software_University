l = int(input())
w = int(input())
h = int(input())
percent = float(input())
volume = l * w * h

all_volume = volume * 0.001
percent = percent * 0.01

liters = all_volume * (1 - percent )

print(f"{liters:.3f}")
