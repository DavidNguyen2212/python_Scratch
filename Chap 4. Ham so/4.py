#1. Hàm có hai kiểu: hàm số có trả giá trị và hàm số không trả giá trị (void hay NoneType trong python)

#2. Định nghĩa
    #2.1. Hàm void
    # def <tên hàm>(<tham số>):
    #   <các lệnh> (có thể có return hoặc không)
def Welcome():
    print("Xin chào!")

    #2.2. Hàm trả giá trị
    # cú pháp y hệt, nhưng bắt buộc CÓ return <giá trị>
def Luythua(x, n, m):
    return (x**n)**m
print(Luythua(2,2,3))

#3. Truyền giá trị
    # Trong python chỉ có truyền tham trị, không có truyền tham chiếu
    # Do python sẽ tạo Namespace của hàm, độc lập với Namespace bên ngoài
    # Do đó, khi viết hàm trong python cần ĐỂ Ý điều đó!!!
n = 5
def tinh(n):
    n = n - 1
    return n    # n ở bên ngoài không bao giờ thay đổi. Thứ ta nhận về chỉ là 1 lvalue!

#4. Định nghĩa hàm trong hàm
    # Các hàm con chỉ có phạm vi sử dụng bên trong hàm cha
    # Tuy nhiên lập trình thực tế ít khi dùng trường hợp này

#5. Phạm vi của biến nhớ và tham biến
    # Xét các ví dụ để hiểu hơn
#vd1: tham số của hàm là n, phân biệt hoàn toàn với n ở toàn cục => ví dụ này dễ hiểu rồi!
n = 2
def f(n):
    n = n + 2
    print(n)

#vd2: MÃ NÀY BỊ LỖI. 
    # Việc lý giải rằng do m chỉ có phạm vi bên trong hàm cha của nó là chưa chính xác. Vd3 sẽ giải thích
    # Lý do thực sự: Lệnh m = m + 2 yêu cầu tạo một biến nhớ mới trong cục bộ g() nhưng lại gán
        #...giá trị là biểu thức m + 2!? => LỖI 
m = 2
def g():
    m = m + 2
    print(m)

#vd3: SỬA LẠI VD2
    # Giải thích: chương trình sẽ tìm giá trị của m bên trong g2() trước (ƯU TIÊN)
    # Tìm không thấy, chương trình sẽ tìm ở toàn cục và tìm được m = 2
m = 2
def g2():
    a = m + 2
    print(a)

#vd4: vd3 có thể viết đơn giản là
def g3():
    print(m + 2)


#6. Tham số thực sự và tham số lựa chọn
    #6.1. Tham số thực sự: là tham số khi gọi hàm ta truyền vào (default argument)
def f1(x, y):       # x và y là TSTS
    return x*y + x-y
f1(2,5)     # 2,5 là các giá trị cho tsts, yêu cầu đúng thứ tự
f1(y = 5, x = 2)    # nếu chỉ rõ tham biến của hàm, truyền như nào cũng được

    #6.2. Tham số lựa chọn: là (các) tham số được gán mặc định trong định nghĩa của hàm.
    #Trong lời gọi hàm có thể vắng mặt tham số lựa chọn tslc, khi đó giá trị mặc định sẽ được sử dụng.
    #Trong hoàn cảnh thông thường, ta vẫn có thể gọi chúng ra và gán giá trị phù hợp được
    # Vd: hàm print có 2 TSLC là sep (mặc định dấu cách) và end (mặc định \n)

print("Hà Nội", "thủ đô", sep = "***", end = "   ")

    #6.3. Cách tạo tham số lựa chọn. (Non-default argument)
    # Liệt kê chúng phía sau tham số thực sự
    # Thêm "= giá trị mặc định"
def power(x, exp = 2):
    return x ** exp

#7. Hàm vô danh: một hàm đơn giản cần định nghĩa nhanh (type là 'function')
    # <tên hàm> = lambda <ds tham số>:<biểu thức tính>
d = lambda x,y : x*x + y*y

#8. Ví dụ khác
# Trong ví dụ Ham_dayso, cho thấy hàm cũng có thể trả về 1 dãy giá trị





