# Chương trình 1, tính USCLN hai số
fin = open("input1.dat", "r")
fout = open("ouput1.dat", "w")
def uscln(m, n):
    while m != n:
        if m < n:
            n = n - m
        else:
            m = m - n 
    return m 
for line in fin:
    x, y = line.split()
    m = int(x)
    n = int(y)
    print("USCLN (", m, ",", n, ") = ", uscln(m,n), file=fout)
fin.close()
fout.close()
