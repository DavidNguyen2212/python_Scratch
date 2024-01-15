# 1. Tổng quan về OOP
    # Hiểu một cách đơn giản: mọi thứ quanh ta đều ẩn chứa mối quan hệ LỚP - Đối tượng
    # Gần nhất trong lập trình: khi khai báo một biến x, x là Đối tượng, còn kiểu dữ liệu của x
    # gọi là LỚP

    # Một lớp có các Thuộc tính (attributes) và Phương thức (methods)
    # Một đối tượng gọi là một thể hiện riêng (instance) của lớp
    # Python là nnlt HƯỚNG ĐỐI TƯỢNG hoàn toàn

# 2. Khởi tạo lớp và đối tượng
class Hocsinh:
    name = "Jenny"
    age = 14
    gender = 1
    school = "THPT Chu Văn An"

    # tạo một đối tượng của lớp này
hs1 = Hocsinh()
hs1.name = "Nguyễn Thị Hoa" # gán giá trị mới cho thuộc tính của đối tượng

    # sử dụng từ khóa self để chỉ bản thân đối tượng (thể hiện của lớp)
class Hocsinh:
    name = "Jenny"
    age = 14
    gender = 1
    school = "THPT Chu Văn An"
    def show(self):
        print("Name = ", self.name)
        print("Age = ", self.age)
        print("Gender = ", self.gender)
        print("School = ", self.school)
    def update(self, name, age, male, school):
        self.name = name
        self.age = age
        self.male = male
        self.school = school

hs2 = Hocsinh()
hs2.show()
hs2.update("Hà", 15, 0, "THCS Chu Văn An")

class BanGhe:
    weight = 60
    height = 100
    length = 180
    color = "Red"
    X = 0
    Y = 0
    def change(self, X, Y):
        self.X = X
        self.Y = Y
    def changeColor(self, color):
        self.color = color
    def changeDim(self, height, width, length):
        self.height = height
        self.width = width
        self.length = length


# 3. Lệnh dir() và __init__()
    # dir(<tên đối tượng hoặc lớp>) hiển thị tất cả thuộc tính và phương thức của nó
    # các phương thức bắt đầu và kết thúc bằng __ đều là của hệ thống. Những thuộc tính / Phương thức
    # ... chúng ta tạo sẽ ở cuối danh sách kết quả
    dir(Hocsinh)
    # Khi cần tra cứu chức năng của phương thức của kiểu dữ liệu builtins => help(lớp.tên phương thức)
    help(str.upper)

    # __init__(): phương thức này có vai trò quan trọng như 1 hàm khởi tạo, nếu có nó thì không cần
    # khai báo thuộc tính bên trong phần mô tả của lớp nữa
    class Hocsinh:
        def __init__(self, name, age, gender, school):
            self.name = name
            self.age = age
            self.gender = gender
            self.school = school
        def show(self):
            print("Name = ", self.name)
            print("Age = ", self.age)
            print("Gender = ", self.gender)
            print("School = ", self.school)

    hs3 = Hocsinh("Hằng", 14, 1, "THCS Trưng Vương")

# 4. Nạp chồng toán tử (overloaded operator)
    # Toán tử chồng có ở tất cả ngôn ngữ lập trình hướng đối tượng. Cùng một toán tử có thể dùng ở nhiều ngữ cảnh 
    # Ví dụ phép + giữa hai số nguyên (kết quả là tổng) khác với phép + giữa hai xâu (nối chuỗi)

# 5. Lớp con và tính kế thừa
    # Tạo lớp cha
    # class <Tên lớp con>(<Tên lớp cha>):
    #   <các mô tả>
    class Tugiac:
        def __init__(self, Name, a, b, c, d):
            self.Name = Name
            self.a = a
            self.b = b
            self.c = c
            self.d = d
        def Chuvi(self):
            return self.a + self.b + self.c + self.d
        
    # Lớp con hình bình hành (kế thừa Tứ giác)
    class Hinh_binh_hanh(Tugiac):
        def __init__(self, Name, a, b, alpha = 45):
            self.Name = Name
            self.a = a
            self.b = b
            self.alpha = alpha
        def Chuvi(self):
            # return super().Chuvi() ta không dùng super vì có cách tính khác
            return 2 * (self.a + self.b)
        def DT(self):
            import math as m 
            return self.a * self.b * m.sin(m.radians(self.alpha))
        
    class Hinh_chu_nhat(Hinh_binh_hanh):
        def __init__(self, Name, a, b):
            self.Name = Name
            self.a = a
            self.b = b
        def DT(self):
            return self.a * self.b 
        
    class Hinh_vuong(Hinh_binh_hanh):
        def __init__(self, Name, a):
            self.Name = Name
            self.a = a
        def DT(self):
            return self.a * self.a 