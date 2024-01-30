import os
os.chdir(r"C:\Users\DELL\Documents\Python3\Chap 10. Doc và ghi tep")
file = open("inp1.dat", "r")
line = file.readline()
A = line.split()
m = int(A[0])
n = int(A[1])
print("Các số đã nhập là: ", m, n)