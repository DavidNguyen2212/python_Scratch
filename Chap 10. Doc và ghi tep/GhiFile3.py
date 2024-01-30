fileout = open("Out2.dat", "w")
msg1 = "The first line."
msg2 = "12 6.7 3.14"
msg3 = "The last line"
A = [msg1, msg2, msg3]
fileout.writelines(A)
fileout.close() # Hoặc ta in cùng lúc vẫn được

