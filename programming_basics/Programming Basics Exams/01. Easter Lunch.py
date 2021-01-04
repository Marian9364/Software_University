cakes = int(input())
eggs = int(input())
cookies = int(input())

cake_price = cakes * 3.20
egg_paint_price = eggs * 12 * 0.15
egg_price = eggs * 4.35
cookies_price = cookies * 5.40

final_price = cake_price + egg_paint_price + egg_price + cookies_price

print(f"{final_price:.2f}")
