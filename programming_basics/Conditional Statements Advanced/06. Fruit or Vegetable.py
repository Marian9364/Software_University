#checking a product

product = input()
is_veggi = product == "tomato" or product == "cucumber" or product == "pepper" or product == "carrot"
is_fruit = product == "banana" or product == "apple" or product == "kiwi" or product == "cherry" or product == "lemon" or product == "grapes"

if is_veggi:
    print("vegetable")
elif is_fruit:
    print("fruit")
else:
    print("unknown")

