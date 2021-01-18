students_count = int(input())
fail_sum = 0
between_3_3_99 = 0
between_4_4_99 = 0
top_students_sum = 0
avg_sum = 0
for grades in range (students_count):
    grade = float(input())
    avg_sum += grade
    if grade < 3:
        fail_sum +=1
    elif 3 <= grade <= 3.99:
        between_3_3_99 += 1
    elif 4 <= grade <= 4.99:
        between_4_4_99 += 1
    elif grade >= 5:
        top_students_sum += 1


top_students_percents = top_students_sum / students_count * 100
between_4_4_99_percents = between_4_4_99 / students_count * 100
between_3_3_99_percents = between_3_3_99 / students_count * 100
fail_sum_percents = fail_sum / students_count * 100
average_percents = avg_sum / students_count

print(f"Top students: {top_students_percents:.2f}%")
print(f"Between 4.00 and 4.99: {between_4_4_99_percents:.2f}%")
print(f"Between 3.00 and 3.99: {between_3_3_99_percents:.2f}%")
print(f"Fail: {fail_sum_percents:.2f}%")
print(f"Average: {average_percents:.2f}")
