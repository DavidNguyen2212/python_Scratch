DS = [["Hà", 8.6, "98976659"], ["Bình", 8.9, "088765544"], ["Hoa", 7.89, "988766555"]]
print("Họ tên:       điểm:          điện thoại")
for hoten,diem,dt in DS:
    s = f"{hoten:<20} {diem: ^6.2f} {dt:>12}"
    print(s)
