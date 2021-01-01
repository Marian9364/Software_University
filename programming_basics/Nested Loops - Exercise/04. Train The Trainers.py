#1. четем презентации до получаване на Finish
count_judges = int(input())
# комнанда -> Finish или име на презентация
command = input()
sum_all_grades = 0
count_grades = 0
#stop: command == Finish; продължаваме: command != Finish
while command != 'Finish':
    #command => име на презентация
    #получаваме си оценки
    sum = 0 #сума за оценките от текущата презентация
    for judge in range(1, count_judges + 1):
        grade = float(input())
        sum += grade
        sum_all_grades += grade
        count_grades += 1
    #сума от оценките за текущата презентация
    #средно аритметичното -> сумата / бр. хората в журито
    average = sum / count_judges
    print(f'{command} - {average:.2f}.')

    command = input()
#command == Finish
#средно аритметично за всички презантации
# = сумата от оценките за всички презентации / брой оценки
average_all_grades = sum_all_grades / count_grades
print(f'Student\'s final assessment is {average_all_grades:.2f}.')
