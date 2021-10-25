products_prices = {}
products_quantities = {}

data = input()
while not data == "buy":
    product, price, quantity = data.split()
    price = float(price)
    quantity = int(quantity)

    if product not  in products_prices:
        products_prices[product] = price
        products_quantities[product] = quantity
    else:
        products_prices[product] = price
        products_quantities[product] += quantity
    data = input()

for product, price in products_prices.items():
    total_price = price * products_quantities[product]
    print(f"{product} -> {total_price:.2f}")
