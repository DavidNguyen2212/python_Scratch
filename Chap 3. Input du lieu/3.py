# 1. thử lệnh input()
name = input("Hãy nhập họ tên: ")
print("Xin chào", name);

# 2. Hàm int(), float(), str() chuyển đổi trực tiếp dữ liệu
    # int() parse được số (biểu thức số) và xâu số nguyên
parse_Int = int(12.55)
parse_Int = int("23")
    # float() parse được số (biểu thức số) và xâu số
parse_Float = float(5)
parse_Float = float("3.1415")
    # str() chuyển 1 giá trị / biểu thức số sang xâu ký tự
    # str() không nhận trực tiếp cặp số (x,y) nhưng nhận được giá trị hàm divmod()
parse_Str = str(3 + 4 * 5 - 17**2)
parse_Str = str(divmod(19,5))

# 3. Hàm eval chuyển đổi xâu biểu thức về dạng số thực (là nguyên nếu kết quả thực sự là nguyên và toán tử đều nguyên)
parse_Expr = eval("24 ** 2 - 15")
    # eval nhận nhiều biểu thức cùng lúc, chách nhawu bởi dấu phẩy
m, n = eval("3, 4**2")

# 4. Kiểu bool và lệnh if
    # bool
    # Hàm bool() kiểm tra giá trị của đối số là True hay False
checkLt = bool(2 < 3)

    # if. Sau điều kiện của if cần có dấu :, cả elif hay else đều như vậy

# 5. Lệnh lặp for
    # sau câu for cần có dấu :
    # range([<start_cond>], <end_cond>, [<increment_expr>]), không bao gồm lần lặp thứ end_cond
n = 100
s = 0
for k in range(1, n+1):
    s = s + k

# 6. Lệnh lặp while
    # sau điều kiện của while cũng có dấu :

