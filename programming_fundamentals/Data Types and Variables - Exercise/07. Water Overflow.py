pour_cnt = int(input())
filled_qnt = 0
for i in range(pour_cnt):
    pour = int(input())
    filled_qnt += pour
    if filled_qnt > 255:
        print("Insufficient capacity!")
        filled_qnt -= pour
        continue
print(filled_qnt)
