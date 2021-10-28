def ascii_inbetweener(sign1, sign2):
    sign1 = ord(sign1)
    sign2 = ord(sign2)
    for i in range(sign1 +1, sign2):
        print(chr(i), end=" ")

ascii_inbetweener(input(), input())
