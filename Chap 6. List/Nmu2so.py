A = []
N = 8
for k in range (1, N + 1):
    A = A + list(range(k, k*N+1, k))
print(A)