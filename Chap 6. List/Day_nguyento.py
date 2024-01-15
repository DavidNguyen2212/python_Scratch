P = []
N = int(input("Nhập số tự nhiên N: "))
count = 0   # Đếm số lượng số nguyên tố
m = 2
while count < N:
    S = 0
    for k in range(1, m):
        if m % k == 0:
            S += 1
    if S == 1:
        P = P + [m]
        count = count + 1
    m = m + 1
print(P)