A = [[10, 12, 21], [1, 17, 100], [210, 420, 99]]
s = "{:5} {:5} {:5}"    # Thiết lập độ rộng các cột
for item in A:
    t0 = item[0]; t1 = item[1]; t2 = item[2]
    print(s.format(t0, t1, t2))