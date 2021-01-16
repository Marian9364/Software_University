n = int(input())
lv_kg = 0

bus_sum = 0
truck_sum = 0
train_sum = 0
vehicle_sum_in_kg = 0
for i in range(1, n +1):
    vehicle_type_from_weight = int(input())
    vehicle_sum_in_kg += vehicle_type_from_weight
    if vehicle_type_from_weight <= 3:
        lv_kg += 200
        bus_sum += vehicle_type_from_weight
    elif 4 <= vehicle_type_from_weight <= 11:
        lv_kg += 175
        truck_sum += vehicle_type_from_weight
    else:
        lv_kg += 120
        train_sum += vehicle_type_from_weight


bus_sum
average_price_per_kg = (bus_sum * 200 + truck_sum * 175 + train_sum * 120) / vehicle_sum_in_kg
microbus = bus_sum / vehicle_sum_in_kg * 100
truck = truck_sum / vehicle_sum_in_kg * 100
train = train_sum / vehicle_sum_in_kg * 100

print(f"{average_price_per_kg:.2f}")
print(f"{microbus:.2f}%")
print(f"{truck:.2f}%")
print(f"{train:.2f}%")
