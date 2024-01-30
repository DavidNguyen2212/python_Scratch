fileout = open("Out2.dat", "w")
msg1 = "The first line."
msg2 = "12 6.7 3.14"
msg3 = "The last line"
print(msg1, file=fileout)
print(msg2, file=fileout)
print(msg3, file=fileout)
fileout.close() # Hoặc ta in cùng lúc vẫn được

