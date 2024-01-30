# Chương trình 2, khai triển số thành dãy các ước nguyên tố
fin = open("input2.dat", "r")
fout = open("output2.dat", "w")
def nguyento(n):
    d = []
    k = 2
    while k <= n:
        i, r = divmod(n, k)
        if r == 0:
            n = i
            d.append(k)
        else:
            k = k + 1
    return d
for line in fin:
    n = eval(line)
    d = nguyento(n)
    for i in d:
        print(i, file=fout, end = " ")
    print(file=fout)
fin.close()
fout.close()