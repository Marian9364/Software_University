#calculating the time from seconds to clock's time

time_a = int(input())
time_b = int(input())
time_c = int(input())

sum_in_sec = time_a + time_b + time_c

minutes = sum_in_sec // 60

seconds = sum_in_sec % 60

if seconds < 10:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")


