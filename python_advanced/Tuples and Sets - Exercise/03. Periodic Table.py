n = int(input())
all_elements_list = []

for _ in range(n):
    list_of_els = input().split()
      
    for el in list_of_els:
        all_elements_list.append(el)
          
set_of_all_elements = set(all_elements_list)

for unique_el in set_of_all_elements:
    print(unique_el)







