F = [1, 1]  # 2 phần tử đầu tiên
N = int(input("Nhập số tự nhiên N: "))
a = F[0]
b = F[1]
for k in range(2, N + 1):
    c = a + b
    F = F + [c]
    a, b = b, c 

print(F)