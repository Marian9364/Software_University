def perfect_number(num):
    num = int(num)
    divisors = 0
    for i in range(1, num):
        if num % i == 0:
            divisors += i
    if divisors == num:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


perfect_number(int(input()))
