# checking if a grade is high enough for a scholarship

import math
income = float(input())
avrg_grade = float(input())
minimum_working_salary = float(input())
scholarship = 0
scholarship_for_excellent_grade = 0

if income < minimum_working_salary and avrg_grade > 4.50:
    scholarship = 0.35 * minimum_working_salary
if avrg_grade >= 5.50:
    scholarship_for_excellent_grade = avrg_grade * 25


if scholarship > 0 and scholarship_for_excellent_grade > 0:
    if scholarship_for_excellent_grade >= scholarship:
        
        print(f"You get a scholarship for excellent results {math.floor(scholarship_for_excellent_grade)} BGN")
    elif scholarship > scholarship_for_excellent_grade:
        print(f"You get a Social scholarship {math.floor(scholarship)} BGN")
elif scholarship > 0 and scholarship_for_excellent_grade == 0:
    print(f"You get a Social scholarship {math.floor(scholarship)} BGN")
elif scholarship == 0 and scholarship_for_excellent_grade > 0:
    print(f"You get a scholarship for excellent results {math.floor(scholarship_for_excellent_grade)} BGN")
else:
    print("You cannot get a scholarship!")
    




