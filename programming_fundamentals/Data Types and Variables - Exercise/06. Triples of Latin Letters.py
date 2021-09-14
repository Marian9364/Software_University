n = int(input())

for i in range (n):
    #print(chr(97),end="")
    for k in range(n):
        #print(chr(98),end="")
        for j in range(n):
            #print(chr(99),end="")
            print(f"{chr(97 + i)}{chr(97 + k)}{chr(97 + j)}")
