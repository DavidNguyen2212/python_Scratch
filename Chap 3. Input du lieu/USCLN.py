M = int(input("Nhập các số tự nhiên m: "))
N = int(input("Nhập số tự nhiên n: "))
m = M; n = N
while n != m:
    if n > m:
        n = n - m 
    else:
        m = m - n 
print("USCLN của", M, "và", N, "là:", n) 