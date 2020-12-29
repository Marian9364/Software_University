start = int(input())
end = int(input())
magic_num = int(input())
combination_counter = 0
is_found = False
for x in range(start, end + 1):
    for y in range(start, end + 1):
        res = x + y
        combination_counter += 1

        if res == magic_num:

            print(f"Combination N:{combination_counter} ({x} + {y} = {magic_num})")
            is_found = True
            break

    if is_found:
        break

if  is_found == False:
    print(f"{combination_counter} combinations - neither equals {magic_num}")
