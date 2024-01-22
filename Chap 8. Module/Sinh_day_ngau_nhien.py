from random import random
N = int(input("Nhập số phần tử của dãy: "))
P = int(input("Nhập giá trị MAX của dãy cần sinh: "))
A = []
for i in range(N):
    A.append(int(P * random()))
print(A)