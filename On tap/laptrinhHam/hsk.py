# sum
print(sum([1,2,3]))

# zip: lặp 2 danh sách cùng lúc
wizards = ['harry', 'ron', 'hermit']
pets = ['cc', 'dd', 'ee']

for wiz, pet in zip(wizards, pets):
    print(f"{wiz} has {pet}")

# sorted
sort_by_first = sorted(['hi', 'hello', 'by', 'CC']) # mặc định sort theo kí tự đầu tiên, dần về sau
sort_by_second = sorted(['hi', 'hello', 'by', 'CC'], key=lambda el:el[1])
print(sort_by_first)
print(sort_by_second)
sort_by_key = sorted([{'name': 'man', 'age':16}, {'name': 'mak', 'age':19}, {'name': 'ann', 'age':10}],
                    key=lambda el:el['name'])
sort_by_age = sorted([{'name': 'man', 'age':16}, {'name': 'mak', 'age':19}, {'name': 'ann', 'age':10}],
                    key=lambda el:el['age'])
print(sort_by_key)
print(sort_by_age)

# mảng 2 chiều
matrix= [[1,2,3], [4,7,8], [9,10,12]]
list_matrix = [matrix[row][col] for row in range(len(matrix)) for col in range(len(matrix[row]))]
list_matrix2 = [ele for row in matrix for ele in row]
print(list_matrix2)
# gộp cột với zip và *, * là toán tử unzip, chuyển dòng thành cột và ngược lại
a = [x for x in zip(*matrix)]
print(a)