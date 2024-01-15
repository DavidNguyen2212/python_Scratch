# 1. Kiểu dữ liệu List
    # như mảng trong C++, chi khác là các phần tử có thể có các kiểu dữ liệu khác nhau
a = [10, 9, 4, 7, "zed"]
type(a) # 'list'

# 2. Phương thức của list
    # len(a): a không chỉ là list mà còn có thể là dãy các giá trị (range...)
len(a)
    # Danh sách rỗng
a = []
    # Phép cộng và * danh sách
    # cộng: nối danh sách, *<số tự nhiên>: cộng <số> lần danh sách lại với nhau
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
d = a * 2
    # Xóa 1 phần tử
    # del a[k] để xóa phần tử thứ k
del c[3]

    # Các phương thức của list
dir(list)   # sách giáo khoa đã ghi rõ cách dùng cơ bản của các phương thức
    # Phân biệt append() và extend()
    # append() bổ sung phần tử và coi nó như là "PHẦN TỬ CUỐI" của danh sách. Nhận kiểu bất kỳ
    # extend() mở rộng danh sách theo đúng nghĩa đen. Chỉ nhận đối tượng là kiểu tuần tự (list, range, tuple)

# 3. Lệnh for trên list
    # Một kiểu dữ liệu tuần tự nếu : có thể truy cập tuần tự && hữu hạn phần tử
    # list, range, tuple, string
    # for <item> in <dữ liệu>:
ds = ["Hà", "Bình", "Huy", "Hoàng", "Thư"]
count = 0
for item in ds:
    count = count + 1
    print(count, item)

# 4. Chỉ số của list
    # a. Chỉ số của list: bắt đầu từ 0. List khác với các kiểu tuần tự khác ở chỗ
    # ... ta có thể sửa các phần tử
a = [1, "Hà Nội", 3.14]
a[0] = 5
a[1] = [0,1]

    # b. Hàm range tổng quát
    # Tạo 1 miền số nguyên thuộc kiểu dữ liệu tuần tự
    # range([<start> = 0], <stop>, [<khoảng cách> = 1]), khoảng cách < 0 để tạo vùng số giảm dần
n = 30
list(range(0, n, 2))
a = list(range(1, n + 1, 1)) + list(range(n-1, 0, -1))

# 5. Kiểu tuple
    # Gọi là dãy số. Gần giống list, nhưng bao bởi ngoặc tròn () và không thay đổi được
    # Phương thức: + , count, index. Chỉ + được hai tuple, không thể list + tuple
a = (1, 2, 3)
b = 12, 3.14, "Hà Nội"