A = [12, 1, 0, 23, 15, 6, 18, 40, 55, 3]
print("Dãy số gốc: ")
print(A)
for i in range (len(A) - 1):
    for j in range (i+1, len(A)):
        if A[i] > A[j]:
            A[i], A[j] = A[j], A[i]
    print(A)
print("Dãy số sau khi đã sắp xếp: ")
print(A)
