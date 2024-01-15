def Tinhtoan(m):
    def Tinh_1(m):
        S = 0
        for i in range(1,m):
            if m % i == 0:
                S = S + 1
        return S
    def Tinh_2(m):
        S = Tinh_1(m)
        if S == 1:
            print(m,"là số nguyên tố!")
        else:
            print(m, "là hợp số.")
        return
    Tinh_2(m)
    return