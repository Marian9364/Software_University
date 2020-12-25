name = input()
all_grades = 0
class = 1

while class <= 12:
    grade = float(input())
    if grade < 4:
        continue
    else:
        all_grades += grade
        class += 1

average_grade = all_grades / 12

print(f"{name} graduated. Average grade: {average_grade:.2f}")
