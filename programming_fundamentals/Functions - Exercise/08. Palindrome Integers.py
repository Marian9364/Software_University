def palindromes(inputing_list):
    for single_item in inputing_list:
        if single_item == single_item[::-1]:
            print("True")
        else:
            print("False")


string_list = input().split(", ")

palindromes(string_list)
