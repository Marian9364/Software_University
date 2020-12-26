bad_grades_allowed = int(input())
grade_sum = 0
problems = 0
bad_grades_count = 0
last_problem = ""
current_problem = ""
while bad_grades_count < bad_grades_allowed:
    last_problem = current_problem
    command = input()
    if command == "Enough":
        break
    else:
        current_problem = command
    grade = int(input())
    if grade <= 4:
        bad_grades_count += 1
    grade_sum += grade
    problems += 1

average_score = grade_sum / problems

if command == "Enough":
    print(f"Average score: {average_score:.2f}")
    print(f"Number of problems: {problems}")
    print(f"Last problem: {last_problem}")
else:
    print(f"You need a break, {bad_grades_count} poor grades.")
# average_score
# number_of_problems
# Last problem
# if bad_grades = bad grades count
