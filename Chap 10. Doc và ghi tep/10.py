# Trong bài này chúng ta làm việc với file txt, dat

# open("đường dẫn đến file", "xâu thao tác");     "xâu thao tác" = "r", "w"
# Thiết lập thư mục làm việc hiện thời:
import os
os.chdir(r"C:\Users\DELL\Documents\Python3\Chap 10. Doc và ghi tep")
file = open("Inp.txt", "r")
# file có kiểu là _io.TextIOWrapper
#s = file.read()
type(file)

# 1. Các lệnh đọc thông tin từ tệp
    # 1.1. open(), read(), close(), tell()
    # Lệnh open tạo ra một đối tượng file. Đầu đọc đang ở vị trí 0
    # open(<file>, "w") sẽ xóa mọi thông tin trong tệp / nếu chưa có file thì tạo file rỗng, tên là file
    # tell cho viết vị trí đầu đọc hiện tại (số byte thông tin đã đọc)
    # close() cần đóng nó lại

    # 1.2. readline()
    # Đọc từng dòng của tệp

    # 1.3. readlines()
    # Đọc hết tệp theo từng dòng, mỗi dòng là một phần tử của list kết quả
    # Nếu đã dùng readline, readlines sẽ đọc hết phần còn lại

    # 1.4. Đọc file như kiểu dl tuần tự
    # tương tự readline nhiều lần vậy. 1 line là 1 dòng
for line in file:
    print(line, end="")

# 2. Lệnh ghi thông tin ra tệp
    # write()
    
    # print()
    # thêm tham số file = <đối tượng file> lệnh print() sẽ không in ra màn hình nữa
    # đặc biệt hỗ trợ \n

    # writelines()
    # Nhận vào danh sách xâu kí tự. Không hỗ trợ \n ở cuối
    

