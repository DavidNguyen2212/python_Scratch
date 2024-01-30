# chương trình đọc file
file = open(r"C:\Users\DELL\Documents\Python3\Chap 10. Doc và ghi tep\Inp.txt", "r")    # Nếu copy nguyên
    # đường dẫn hãy dùng tiền tố r (raw), nếu không phải dùng \\ thay cho \
content = file.read()
print(content)

file = open("Chap 10. Doc và ghi tep\\Inp.txt")
content = file.read()
print(content)
# import os

# current_directory = os.getcwd()
# print("Đường dẫn thư mục hiện tại:", current_directory)

