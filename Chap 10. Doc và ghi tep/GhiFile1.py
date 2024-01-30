fileout = open("Out1.dat", "w")
msg1 = "The first line."
msg2 = "12 6.7 3.14"
msg3 = "The last line"
fileout.write(msg1)
fileout.write(msg2)
fileout.write(msg3)
fileout.close() # lệnh write k hỗ trợ xuống dòng. Ta cần tự thêm \n