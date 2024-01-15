A = [2, 19, 30, 45, 100, 101, 103, 257, 890, 1001, 10101]
B = []
for item in A:
    S = 0
    for i in range (1, item):
        if item % i == 0:
            S = S + 1
    if S == 1:
        B = B + [item]
print("Dãy A:")
print(A)
print("Dãy B:")
print(B)
