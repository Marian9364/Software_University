#Calculating the final price of pieces of clothes

table_counter = int(input())
lenght_tables = float(input())
width_tables = float(input())
table_cloth_lenght = lenght_tables + (2 * 0.30)
table_cloth_width = width_tables + (2 * 0.30)
table_cloth_size = table_cloth_lenght * table_cloth_width
table_cloth_price_in_dollars = table_cloth_size * 7

kare_lenght = lenght_tables / 2
kare_width = lenght_tables / 2
kare_size = kare_lenght * kare_width
kare_price = kare_size * 9

final_price_dollars = (table_cloth_price_in_dollars + kare_price) * table_counter
final_price_leva = final_price_dollars * 1.85
print(f"{final_price_dollars:.2f} USD")
print(f"{final_price_leva:.2f} BGN")
