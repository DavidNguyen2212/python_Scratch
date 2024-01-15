a = []
for i in range(1, 101):
    a = a + [i] # nối danh sách chỉ có 1 phần tử i vào danh sách
print(a)

# Hoặc sử dụng biểu thức list comprehension để tạo danh sách:
a = [i for i in range(1, 101)]
