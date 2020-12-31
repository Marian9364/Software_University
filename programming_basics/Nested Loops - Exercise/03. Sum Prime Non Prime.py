#1. четем числа докато не получим stop
command = input() #-> "3" или stop

#стоп -> command == stop
#продължаваме -> command != stop
sum_prime = 0 #сума от прости числа (делителите = 2)
sum_no_prime = 0 #сума от съставните числа (делителите > 2)

while command != 'stop':
    #command -> число под формата на текст -> '5' -> число
    number = int(command)
    #1. да е отрицателно
    if number < 0:
        print('Number is negative.')
    else:
        #2. да е положително -> просто или съставно
        count = 0 #брой на делителите
        for i in range(1, number + 1): #[1; number]
            if number % i == 0:
                count += 1
        # знаем колко е броят на делителите
        #проверка
        if count == 2:
            #просто
            sum_prime += number
        elif count > 2:
            #съставно
            sum_no_prime += number
    command = input()
#принтираме двете суми
print(f'Sum of all prime numbers is: {sum_prime}')
print(f'Sum of all non prime numbers is: {sum_no_prime}')
