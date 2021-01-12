pencils = int(input())
markers = int(input())
cleaner = float(input())
discount_percentage = int(input())

summ = 0
pencils_price = pencils * 5.80
markers_price = markers * 7.20
cleaners_price = cleaner * 1.20

summ = pencils_price + markers_price + cleaners_price

final_price = summ - ((summ * discount_percentage) / 100)
print(f"{final_price:.3f}")
