a = []
m = int(input("Nhập số tự nhiên m: "))
n = int(input("Nhập số tự nhiên n: "))
for i in range(m):
    print("Chuẩn bị nhập ma trận hàng thứ", i+1, ":")
    b = []
    for j in range(n):
        x = int(input("Nhập phần tử thứ " + str(j+1) + ": "))
        b = b + [x]
    a.append(b)
print("Ma trận A đã nhập xong!")
# in ma trận ra màn hình
for i in range(m):
    for j in range(n):
        print(a[i][j], end=" ")
    print()