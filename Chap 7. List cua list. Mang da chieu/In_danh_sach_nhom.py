A = [["Xanh", "Bình", "Hà", "Sơn", "Thuận"],
     ["Đỏ", "Hiền", "Công", "Thành"],
     ["Tím", "Thành B", "Huy", "Dương", "Trần", "Cường"],
     ["Vàng", "Hoa", "Hồng", "Anh", "Thịnh", "Hiệp", "Hoàng", "Yến"]]

for i in range(len(A)):
    print("Nhóm", A[i][0], ": ", sep="")
    print("      ", end="")
    for j in range (1, len(A[i])):
        print(A[i][j], ", ", sep="", end="")
    print()