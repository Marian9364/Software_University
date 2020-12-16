#calculating all of the products and printing out the sum 

days = int(input())
ppl = int(input())
cakes = int(input())
waffles = int(input())
paincakes = int(input())

cakes_price = cakes * 45 * days * ppl

waffles_price = waffles * 5.80 * days * ppl
paincakes_price = paincakes * 3.20 * days * ppl

summ = cakes_price + waffles_price + paincakes_price

summ = summ - (summ * 0.125)

print(f"{summ:.2f}")
