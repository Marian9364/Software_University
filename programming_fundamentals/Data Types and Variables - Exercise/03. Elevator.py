n = int(input())
capacity_p = int(input())
courses_made = 0
if n > capacity_p:
    courses_made = n // capacity_p
    rest_ppl = n % capacity_p
    if rest_ppl != 0:
        courses_made += 1
elif n <= capacity_p:
    courses_made = 1

print(courses_made)



