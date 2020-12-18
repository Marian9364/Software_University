import math
record = float(input())
lenght_in_m = float(input())
time_in_sec_for_m = float(input())

time_in_sec = lenght_in_m * time_in_sec_for_m

slowing = lenght_in_m / 15
slowing_rounded = math.floor(slowing) * 12.5
time_sum = time_in_sec + slowing_rounded
diff = abs(time_sum - record)

if time_sum < record:
    print(f"Yes, he succeeded! The new world record is {time_sum:.2f} seconds.")
else:
    print(f"No, he failed! He was {diff:.2f} seconds slower.")
