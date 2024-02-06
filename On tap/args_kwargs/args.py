def printName(name: str) -> str:
    print(name)

def codeXplore(a, b, c):
    print(a, b, c)
def main():
    printName("CodeXplore")
    codeXplore(3,2,1)   # tham số theo vị trí (đúng thứ tự hàm)
    codeXplore(b = 2, a = 3, c = 4) # tham số keyword: gán giá trị kèm với

    # args example
    #variableLengthArgExample('a', 'b')
    #variableLengthArgExample('c', 'd', 'ddd', 123, (2,3))

    # kwargs example
    variableLengthKWArgExample('a', 2, size = "XXL",c = "lvalue", age=16)

# *args và **kwargs là gì? - variable length params
# vd: một mô tả hàm: http_method_not_allowed(request, *args, **kwargs)
# còn ở phương thức khởi tạo có thể đặt là **initkwargs, *initargs để thống nhất 
# *args: bạn có thể pass vào một số lượng tùy ý tham số theo vị trí
def variableLengthArgExample(a,b, *args):   # tuple
    print(a,b, end= " ")
    for arg in args:
        print(arg, end=" ")
    print()
    
def variableLengthKWArgExample(a,b, **kwargs):    # dict[str, any]
    print(a,b, end= " ")
    for param, value in kwargs.items():
        print(f"{param}: {value}")

if __name__ == "__main__":
    main()