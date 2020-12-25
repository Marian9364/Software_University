name = input()
all_grades = 0
clas = 1
expelled = 0

while clas <= 12:
    grade = float(input())
    if grade < 4:
        expelled += 1
        if expelled > 1:
            break
        continue
    else:
        all_grades += grade
        clas += 1

average_grade = all_grades / 12
if expelled > 1:
    print(f"{name} has been excluded at {clas} grade")
else:
    print(f"{name} graduated. Average grade: {average_grade:.2f}")
