# 1. Lệnh import
    # hàm hệ thống nằm trong lõi gốc python ở __builtins__
    # Muốn sử dụng một module (các hàm của nó) ta import
import math
    # (!) module.tên_phương_thức
a = math.sqrt(2)
    # Nếu không muốn (!) thì phải from <module> import <hàm>/*
from math import *;
b = sqrt(9)
    # Nhập khẩu nhiều thư viện
import math, matplotlib, matplotlib_inline
    # Nhập khẩu sử dụng alias
import math as m 
c = m.sqrt(16)

# 2. Module math
dir(math)
# 3. Số phức và module math
    # phần thực + phần ảo j. phần ảo = 1 / -1 vẫn phải viết 1 / -1
z = 1 + 1j
dir(z)
from cmath import *     # cmath hỗ trợ tính toán với số phức

# 4. Tự tạo module
from module_1 import *
f1(5)

# 5. Sinh số ngẫu nhiên trong Python
    # hàm random của module random sinh số (thực) ngẫu nhiên từ  [0, 1)
from random import random;
random()
    # Sinh số nguyên từ [0, 100] 
z = int(101 * random())
    # Sinh số thực từ [0, 100)
x = 100 * random()
    # Sinh số nguyên ngẫu nhiên trong đoạn [M, N]: 
M = 30
N = 40
y = int(M + (N+1-M) * random())

# 6. Sinh giá trị ngẫu nhiên từ 1 dãy
    # choice(<dãy giá trị tuần tự>) list, tuple, range, xâu, LC
import random as r
A = [0, 4, 19, 700]
r.choice(A)
s = "Thu do Ha noi"
s0 = r.choice(s)
    # randint(a,b): sinh số nguyên trong đoạn [a, b]
n = r.randint(10, 20)
    # randrange(start, stop, step) sinh số thuộc lệnh range tương ứng
n = r.randrange(0, 100, 2)
