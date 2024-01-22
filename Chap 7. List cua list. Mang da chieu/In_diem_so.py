D = [["Hà", [6,7,9], [7, 3, 10, 6]], 
     ["Đức", [10, 9, 10, 8], [6, 8, 7]], ["Ngọc", [7, 10, 9], [10, 6, 5, 5, 9]]]
for ten, diem1, diem2 in D:
    print(ten);
    print("\tHệ số 1: ", end="   ")
    for diem in diem1:
        print(diem, end="   ")
    print()
    print("\tHệ số 2: ", end="   ")
    for diem in diem2:
        print(diem, end="   ")
    print()