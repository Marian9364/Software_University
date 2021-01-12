fruit = input()
size = input()
sets = int(input())
price_for_small = 0
price_for_big = 0
discount = 0
price_for_set = 0
if fruit == "Watermelon":
    price_for_small = 56 * 2
    price_for_big = 28.70 * 5
elif fruit == "Mango":
    price_for_small = 36.66 * 2
    price_for_big = 19.60 * 5
elif fruit == "Pineapple":
    price_for_small = 42.10 * 2
    price_for_big = 24.80 * 5
elif fruit == "Raspberry":
    price_for_small = 20 * 2
    price_for_big = 15.20 * 5

if size == "big":
    price_for_set = price_for_big
elif size == "small":
    price_for_set = price_for_small

price_for_set *= sets

if 400 <= price_for_set <= 1000:
    discount = price_for_set * 0.15
elif price_for_set > 1000:
    discount = price_for_set * 0.5
price_for_set -= discount
print(f"{price_for_set:.2f} lv.")
