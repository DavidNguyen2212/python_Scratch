A = ["Oanh", "Thanh", "Ba", "Rinh", "Quang", "Hanh", "Vinh", "Hoa", "Loan", "An"]
def SapXep(sA):
    DS = sA
    for i in range(len(DS) - 1):
        for j in range(i+1, len(DS)):
            if DS[i] > DS[j]:
                DS[i], DS[j] = DS[j], DS[i]
    return DS
print("Danh sách gốc: ")
print(A)
print("Danh sách đã sắp xếp: ")
print(SapXep(A))