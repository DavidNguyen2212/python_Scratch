# 1. Các vòng lặp lồng nhau. Tìm hiểu sâu hơn các tính năng của for với lệnh list
m = 4; n = 6
for i in range (m):
    for j in range (n):
        print("(", i+1, ", ", j+1, ")", sep="", end=" ")
    print()

# 2. List của list
    # có dạng như sau: A = [<list1>, <list2>, ..., <list N>]

# 3. Dữ liệu có cấu trúc
    # Dữ liệu có cấu trúc là một bộ dữ liệu được sắp xếp và ghép lại theo một quy luật nào đó
    # Lệnh gán đồng thời với list
a = [1, 2, 3]
x, y, z = a # Khi đó x = 1, y = 2, z = 3
    # For trong list of list: nếu list con có pt1, pt2,...ptn thì ta for một lúc n phần tử này được ngay
A = [["Bình", 2010, "Hà Nội"], ["Sơn", 2011, "Thái Bình"], ["Quang", 2008, "Quảng Nam"]]
# cấu trúc chung là ten, nam, quequan
for ten, nam, quequan in A:
    print("Tên hs:", ten, ", Năm sinh:", nam, ", Quê quán:", quequan)

# 5. Chỉ số âm và vùng chỉ số
    #a. Chỉ số âm của list, tuple, string, range
    # Chỉ số dương từ 0 -> len-1; âm đi từ -len về -1
a = ["One", "Two", "Three", 4, 5, 6]
a[-6]

    # Vùng chỉ số (slicing)
    # a[<start> = 0 : <stop> = len(a)], không lấy stop
newlist = a[2:]
a[0:2] = "a", "b"   # phép gán thông thường cũng có thể thực hiện trên vùng chỉ số
    # mở rộng a[<start>:<stop>:<increment = 1>] 
    # nếu incre > 0,<start> = 1, <stop> = len(a);
    # nếu incre < 0, <start> = -1, <stop> = -len(a) - 1

# 6. Liên kết tham biến của list
    # toán tử is kiểm tra 2 "Đối tượng số" có giống nhau hay không
x = 5
y = x
x is y
    # Ta đã biết nếu truyền 1 biến toàn cục vào hàm thì không ảnh hưởng gì biến đó.
    # Nhưng nếu biến đó là 1 list thì sẽ có chuyện xảy ra!?
    # Tóm lại: nếu chỉ thay đổi (cấp độ phần tử) list x thì y và x giống nhau. 
        # Nhưng nếu thực hiện phép gán hoàn chỉnh (cấp độ x, y) thì x,y không còn giống nhau
    # Khi truyền list vào hàm: 
        # thay đổi cấp độ x thì list x sẽ không đổi
        # thay đổi cấp độ phần tử => x thay đổi

# 7. List comprehension (LC)
    # Tức là mỗi phần tử của list sẽ được sinh bằng công thức ngắn gọn (dễ hiểu)
    # list_mới = [<công thức> for item in <list_cho_trước>]
xlist = [1,2,3,4,5,6]
ylist = [item * item for item in xlist]

# 8. Iterable data object
    # Ngoài list, tuple, xâu, range, LC thì ta cũng có một generator tương tự LC nhưng để trong dấu ()
G = (2*i for i in range(10)) # G là một generator, nhưng chỉ dùng được 1 lần.
    # Ta sử dụng hàm sinh tuần tự với yield
def OddNum(n):
    for i in range(n):
        yield 2*i + 1

n = 20
for k in OddNum(n):
    print(k, end = " ")


