clothes_in_box = list(map(int, input().split()))
one_rack_capacity = int(input())
constant_one_rack_capacity = one_rack_capacity
racks = 1


while clothes_in_box:

    last_piece_of_clothing = clothes_in_box.pop()
    if one_rack_capacity >= last_piece_of_clothing:
        one_rack_capacity = one_rack_capacity - last_piece_of_clothing
    else:
        
        racks += 1
        one_rack_capacity = constant_one_rack_capacity
        clothes_in_box.append(last_piece_of_clothing)


print(racks)
