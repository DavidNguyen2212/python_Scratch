'''
1. type <data> trả lại kiểu dữ liệu hiện thời của data
2. Các biến không cần khai báo trước kiểu dữ liệu. Nó linh hoạt thay đổi theo dữ liệu ta gán
3. Tính toán số học: +, -, *, / (chia thực), // (chia nguyên), % (mod), ** (lấy lũy thừa)
2 ** 3 ** 4 thực hiện xếp chồng và tính toán = 2 ** (3 ** 4)
4. Tên biến nhớ bắt đầu bằng chữ cái hoặc dấu _, không được phép là chữ số
5. Lệnh gán
    <biến nhớ> = <giá trị>
6. Việc gán đồng thời có thể thực hiện:
    x,y,z = 1,2,3
    Đặc biệt, hoán đổi hai biến không cần temp!
    x, y = y, x
7. Các phép gán thay đổi: x += 1, y -= x... tuy nhiên trong python bản chất hai lệnh x+= 1 và x = x + 1
này là khác nhau.
8. Từ khóa trong python: chú ý kí tự _ là biến nhớ đặc biệt, luôn chứa giá trị của biểu thức gần đây nhất
9. Viết lệnh trên nhiều dòng:
- Dùng dấu sau đó xuống dòng
- Nếu đã mở ngoặc (, thì ta xuống dòng viết bình thường.
- Khi nhập một xâu kí tự, nếu xâu đó qua dài dùng 3 dấu quotes.
10. Hàm divmod
divmod(x,y) = x // y, x % y

Bài 1: Vì tên biến tách rời kiểu dữ liệu (cơ chế namespace), tên biến không thay đổi khi giá trị đối
tượng trong Object thay đổi. Biến nhớ nhận được nhiều giá trị khác nhau
Bài 2: hàm trong python 
'''
