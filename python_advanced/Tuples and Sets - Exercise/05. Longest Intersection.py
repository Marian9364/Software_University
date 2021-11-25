n = int(input())
  
list_1 = []
list_2 = []
current_intersection = []
new_longest_longest_intersection = []

for _ in range(n):
    ranges = input().split("-")
    first_range = ranges[0].split(",")
    second_range = ranges[1].split(",")
    for num in range(int(first_range[0]), int(first_range[1]) + 1):
        list_1.append(num)

    for num in range(int(second_range[0]), int(second_range[1]) + 1):
        list_2.append(num)
    set_1 = set(list_1)
    set_2 = set(list_2)
    current_intersection = set_1.intersection(set_2)
    if len(current_intersection) > len(new_longest_longest_intersection):
        new_longest_longest_intersection = current_intersection
    list_1 = []
    list_2 = []
    
list_output = list(new_longest_longest_intersection)
print(f"Longest intersection is {list_output} with length {len(new_longest_longest_intersection)}")













