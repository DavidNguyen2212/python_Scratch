def Nguyento(m):
    S = 0
    for i in range (1, m):
        if m % i == 0:
            S = S + 1
    if S == 1:
        return 1
    else:
        return 0
    
m =  int(input("Nhập số tự nhiên m: "))
if Nguyento(m) == 1:
    print(m, "là số nguyên tố")
else:
    print(m, "không là số nguyên tố")
        