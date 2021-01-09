bitcoin = int(input())
chinese_iuan = float(input())
komission= float(input())

summ = 0
bitcoin *= 1168
chinese_iuan *= 0.15
chinese_iuan *= 1.76

summ = (bitcoin + chinese_iuan) / 1.95
comision = komission * 0.01
finall_comision = summ * comision
final_sum = summ - finall_comision
print(f"{final_sum:.2f}")
