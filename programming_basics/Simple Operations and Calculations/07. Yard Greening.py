kmeters = float(input())

summ = kmeters * 7.61

discount = summ * 0.18

end_sum = summ - discount

print(f"The final price is: {end_sum:.2f} lv.")
print(f"The discount is: {discount:.2f} lv.")
