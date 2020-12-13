# calculating the area of a 2d rectangle

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

side_x = abs(x1 - x2)
side_y = abs(y2 - y1)

volume = side_x * side_y
summ = side_y + side_x

summm = 2 * summ

print(f"{volume:.2f}")
print(f"{summm:.2f}")
