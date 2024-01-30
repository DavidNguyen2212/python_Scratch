# 1. String
    # Một xâu không cho phép bạn thay đổi dữ liệu của nó
    # Mọi đối tượng dữ liệu đều có thể thành string bằng hàm str()
n = 100
x = 3.1514
a = [1, 2, "One", [3,4]]
s = str(n) + str(x) + str(a)
print(s)

# 2. Bảng mã ascii và unicode
    # Hàm ord và chr()
ord("A")    # ký tự -> unicode; 
ord("Á")
chr(7848)   # unicode -> kí tự
    # ord(chữ hoa) + 32 = ord(chữ thường)
def f_hoa(s):
    kq = ""
    for ch in s:
        kq = kq + chr(ord(ch) - 32)
    return kq

    # Phép so sánh "thứ tự từ điển":
        # 1. ký tự ch1 < ch2 <=> mã hóa ord(ch1) < ord(ch2)
        # 2. Xâu s1 < s2 nếu kí tự khác nhau đầu tiên của hai xâu (tính từ trái qua) thỏa quan hệ 1.

# 3. Dãy thoát (escape)

# 4. Các phương thức của xâu
    # a. Chữ hoa chữ thường
s = "Last Friday over 4 million people striked for the climate"
s1 = s.upper()
s2 = s.lower()
s3 = s.capitalize()
s4 = s.title()
s5 = s.swapcase()

    # b. Khoảng trắng thừa, kể cả escape
s = "  Hà Nội   "
s6 = s.strip()
s7 = s.lstrip()
s8 = s.rstrip()

    # c. count(<chuỗi cần tìm>, [start, end]): tìm số lần lặp (không chồng lấn) của chuỗi cần tìm
        # trong chuỗi mẹ trong vùng chỉ số [start, end]. vùng chỉ số này tương tự như ở list
        # việc tìm kiếm có phân biệt thường hoa
s = "ababababab"
s9 = s.count("a")
s10 = s.count("aba")
    
    # d. find() và index()
        # trả về chỉ số đầu tiên tìm thấy xâu con
        # hai hàm giống nhau, nhưng khi không tìm thấy
            # find trả về -1
            # index trả về giá trị "substring not found" cho biến ValueError
        # cú pháp đầy đủ cũng có start, end như count()
s = "001122334455"
s.find("12")
s.index("12")
s.find("123")
s.index("123")

    # e. replace(<old>, <new>, [count = -1])
    # thay thế old trong xâu mẹ bằng new. số lần thay: count, mặc định -1 là thay thế tất cả
s = "ababababab"
s.replace("a", "A", 2)
s.replace("b", "C")

    # f. split() và join()
        # split() tách xâu kí tự thành danh sách các xâu con
            # Mặc định: phân tách thông qua khoảng trắng (bao gồm cả chuỗi thoát)
s = "Hà   Nội là , Thủ đô của nước Việt \nNam"
s.split()
            # split([sep = none, maxsplit = -1]), sep là kí tự phân cách. maxsplit: số thành phần tối đa có 
            # được từ phép tách. Nếu dư, nguyên phần còn lại sẽ được mang vào kết quả (gồm maxsplit + 1 phần tử)
s.split(4)
        # s.join(str) để gộp kiểu dữ liệu tuần tự str (str hoặc danh sách str) thông qua kí tự kết nối s.  

    # g. Hàm __repr__(): có sẵn ở mọi đối tượng python. trả về dạng xâu ký tự hình ảnh gốc của đối tượng
a = [1, 2, 3, 4]
a.__repr__()

# 5. PHƯƠNG THỨC tạo khuôn (format)
    # Định nghĩa placeHolder / field: là một cặp {}
    # a. Thay thế đơn giản không chỉ số
s = "Đây là các số {}, {}, {}"
s.format(1, 2, 3)   # số tham số của hàm format >= số field

s = "Học sinh thứ {} tên là {}"
HS = ["Hà", "Bình", "Quang", "Vinh", "Việt", "Cường"]
for i in range(len(HS)):
    print(s.format(i+1, HS[i]))

    # b. Thay thế tự động với chỉ số
    # thứ tự chỉ số trong lệnh format bắt đầu từ 0
    # để chỉ định một field gắn với chỉ số, ví dụ {} ứng với tham số thứ 1 => {1}.
m = 15
n = 50
s = "Cho trước các số {0}, {1}. Cần tìm ước số chung của {1} và {0}"
s.format(m, n)

    # c. Chỉ lệnh trong field
    # field = {[<chỉ số>]:[<chỉ lệnh>]}, có thể viết {:[chỉ lệnh]} cũng được

    # c1. Chỉ lệnh thiết lập Width
    # lúc này chỉ lệnh là số tự nhiên > 0, là độ dài của vùng thể hiện
    # Mặc định kiểu xâu sẽ căn trái, kiểu số căn phải trong vùng thể hiện
s = "Các giá trị a = {:5}, b = {:5}, c = {:5}"
s.format(1, 3, 6)

    # c2. Chỉ lệnh căn chỉnh thẳng hàng
    # field = {[<chỉ số>] : <ký hiệu căn><width>}. Ví dụ: {0:<10}
    # ký hiệu: = (căn đều hai bên), ^ căn giữa, < căn trái, > căn phải
s = "{0:<10} {0:^10} {0:>10}"
s.format(1234)

    # c3. Chỉ lệnh chèn kí tự vào khoảng trống
    # field = {[<chỉ số>] : <char><ký hiệu căn><width>}.
s = "{0:-<10} {0:*^10} {0:+>10}"
s.format(1234)  # KQ: '1234------ ***1234*** ++++++1234'

    # c4. Chỉ lệnh cho số gần đúng (precision, maximum width)
    # field = {[<chỉ số>] : <width>.<p>}. p là số chữ số. Nếu số thập phân là 0.xxxx => p = số chữ số
    # sau dấu phẩy, còn lớn hơn 1 thì p là tổng số chữ số sau dấu phẩy
s = "{:.5}" # width tự do
s.format(1.344677777)
    # p đối với xâu kí tự: độ dài tối đa. Nếu vượt quá sẽ bị cắt bớt
s = " {:<10.5} {:<10.5} {:<10.5} "
s.format(0.3456789, "Hà Nội", "Việt Nam")

    # c5. Chỉ lệnh hash. Viết trước width.p để điền thêm số 0 bên phải, đủ chiều dài p
s = "{:10.5} {:#10.5}"
s.format(0.12, 0.4)

    # c6. Chỉ lệnh kiểu
    # là b (nhị phân), c (unicode), d (số nguyên), f (số thập phân cố định), e (biểu diễn e), g(dạng tổng quát
    # nhất do python chọn)
s = "{0:b} {0:c} {0:d}"
s.format(66) 
s1 = "{0:b} {0:d} {0:f} {0:e}"
s1.format(65.2) # lỗi vì python ko diễn dịch được 65.2 về binary

    # c7. Chỉ lệnh dấu phẩy hình thức
    # Viết ngay trước dấu ., sau width. ngăn cách các nhóm 3 chữ số
s = "{0:,.5e} {0:,.5f}"
s.format(100022800.234555)

    # c8. Tổng quát về chỉ lệnh
# Field = {<chỉ số> : <space> <=> <#> <width> <,> <.> <p> <type>}
        # space là kí tự bất kì để chèn các khoảng trống (mặc định)
        # = là kí tự căn thẳng hàng: = < > ^
        # # là kí tự hash điền thêm 0 để có đủ chiều dài p
        # width: độ rộng thể hiện của số
        # , là dấu phẩy hình thức
        # . ngăn cách width và p
        # p là số các chữ số thập phân
        # type là chỉ lệnh kiểu: b,c,d,e,f

# 6. LỆNH format
    # format(<đối tượng cần format>, <xâu chỉ lệnh điều khiển>)
format(123, "b")
format(0.123456789, "0<10.3")

# 7. Tạo khuôn bằng f-string
    # Gần giống như phương thức format nhưng thực hiện ngay tại chỗ
    # s = f"{<var1>:<chỉ lệnh>} {<var2>:<chỉ lệnh>} {<var3>:<chỉ lệnh>}
hoten = "Bui Viet Ha"
diem = 8.9
dt = "012344444"
s = f"Họ tên: {hoten:<15} điểm: {diem:5.2f} điện thoại {dt:>10}"
