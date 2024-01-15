HS = []
N = int(input("Nhập số học sinh trong lớp: "))
for i in range(1, N+1):
    s = input("Nhấp tên học sinh thứ " + str(i) + ": ")
    HS = HS + [s]
print("Danh sách học sinh đã nhập: ")
for i in range(1, N+1):
    print(i, HS[i-1])