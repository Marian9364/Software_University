flour_price_per_kg = float(input())
kg_flour = float(input())
kg_sugar = float(input())
eggs = int(input())
backpulver = int(input())

sugar_price = flour_price_per_kg * 0.75
eggs_price = flour_price_per_kg * 1.10
backpulver_price = sugar_price * 0.20

flour_sum = flour_price_per_kg * kg_flour
sugar_sum = sugar_price * kg_sugar
egg_sum = eggs * eggs_price
backpulver_sum = backpulver * backpulver_price
final_price = flour_sum + sugar_sum + egg_sum+ backpulver_sum
print(f"{final_price:.2f}")
