def fixTyping(s):
    a = s.split()
    return " ".join(a)
s = input("Nhập một chuỗi bất kỳ: ")
print("Xâu đã sửa lỗi là: ")
print(fixTyping(s))