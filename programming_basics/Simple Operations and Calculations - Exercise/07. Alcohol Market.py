#calculating the sum of all the drinks bought from an alcohol market

whiskey_price = float(input())
beer = float(input())
wine = float(input())
rakia = float(input())
whiskey_count = float(input())

rakia_price = whiskey_price / 2
wine_price = rakia_price * 0.60
beer_price = rakia_price * 0.20

whiskey_summ = whiskey_price * whiskey_count
beer_summ = beer * beer_price
rakia_summ = rakia_price * rakia
wine_summ = wine * wine_price

summ = whiskey_summ + beer_summ + rakia_summ + wine_summ

print(f"{summ:.2f}")
