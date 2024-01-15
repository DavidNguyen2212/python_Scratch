def Dayso(m):
    S1 = S2 = 0
    # Tất cả các ước gồm cả 1
    for i in range(1,m):
        if m % i == 0:
            S1 = S1 + 1
    
    # Chỉ lấy các ước là số nguyên tố
    for k in range(2,m):
        if m % k == 0:
            s = 0
            for i in range (1, k):
                if k % i == 0:
                    s = s + 1
            if s == 1:
                S2 = S2 + 1
    return S1, S2

m = int(input("Nhập số tự nhiên m: "))
print(Dayso(m))
        