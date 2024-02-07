# Hàm lambda không cần có tên, viết trên một dòng
codeXplore = lambda x,y,z : x + y - z
print(codeXplore(3,4,5))

# Hàm lambda như là key của hàm sorted
coordinate = [(6,9), (9,6), (-1,3), (3,1)]
print(sorted(coordinate))   # thông thường xếp theo x
print(sorted(coordinate, key=lambda point: point[1]))

arr = [5,3,-2,-1,-99]
print(sorted(arr))
print(sorted(arr, key=lambda x: abs(x)))

# Hàm map
    # map(func, seq)
list_keyword = ["code", "anna", "jasmine", 'vietnam']
# hàm  map chỉ trả về map object. ta cần dùng hàm list để có được danh sách thực sự
print(list(map(lambda x: x.title(), list_keyword)))

# Hàm filter
    # filter(assert_Func, seq) trả về object có các phần tử thỏa assert_Func
list_num = [1,2,3,4,5,6,7,8]
print(list(filter(lambda x: x%2 != 0, list_num)))
        # map, filter cũng có hiệu quả tương tự list comprehension

# Hàm reduce
    # reduce(func, seq) lặp đi lặp lại áp dụng func lên các phần tử, trả về giá trị đơn
    # func phải là 1 hàm nhận 2 tham số
from functools import reduce
seq = [1,2,3,4,5,6,7,8,9]
print(reduce(lambda a, b: a + b, seq))
print(reduce(lambda a, b: a + b, seq, 1))
print(reduce(lambda a, b: a if a > b else b, seq))      # if else trong lambda
