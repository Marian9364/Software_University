#Console program about greening an Yard
kmeters = float(input())

sum_ = kmeters * 7.61

discount = sum_ * 0.18

end_sum = sum_ - discount

print(f"The final price is: {end_sum:.2f} lv.")
print(f"The discount is: {discount:.2f} lv.")
