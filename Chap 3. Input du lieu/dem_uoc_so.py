n = int(input("Nhập số tự nhiên n: "))
count = 0
for k in range(1, n):
    if n % k == 0:
        count += 1
print("Số các ước số thực sự của", n, "là:", count)