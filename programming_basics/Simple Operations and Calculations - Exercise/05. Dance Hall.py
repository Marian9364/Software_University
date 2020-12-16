#calculating the space in a dance hall

import math
L = float(input())
W = float(input())
wardrobe_side_a = float(input())

hall_size = (L * 100) * (W * 100)

wardrobe_side_a_in_cm = wardrobe_side_a * 100
wardrobe_size = wardrobe_side_a_in_cm * wardrobe_side_a_in_cm

bench_size = hall_size / 10
free_space = hall_size - bench_size - wardrobe_size
dancers = free_space / (40 + 7000)

print(math.floor(dancers))
