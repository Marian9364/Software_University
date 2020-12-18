#turning hours + minutes + 15 minutes into clock's time

hours = int(input())
minutes = int(input())
hours_in_min = hours * 60 + 15
sum_of_min_and_hours = hours_in_min + minutes

hours_after_calc = sum_of_min_and_hours // 60
mins_after_calc = sum_of_min_and_hours % 60

if hours_after_calc >=24:
    hours_after_calc = 0

if mins_after_calc < 10:
    print(f"{hours_after_calc}:0{mins_after_calc}")
else:
    print(f"{hours_after_calc}:{mins_after_calc}")
