list_1 = input().split(", ")
list_2 = input().split(", ")
result_list = []
for word in list_1:
    for words in list_2:
        if word in words:
            if word not in result_list:
                result_list.append(word)

print(result_list)
