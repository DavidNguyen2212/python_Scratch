# Xác định xem string có các kí tự phân biệt hay không
import unittest as unt

# inherit lớp testcase của module unittest
class Test(unt.TestCase):
    dataTrue = ['abcd', '123456','s432adghij', ('')]
    dataFalse = [('232ds2'), ('hb dahfhfhk1')]
    def test_unique(self):
        # true
        for test_case in self.dataTrue:
            actualResult = unique(test_case)
            self.assertTrue(actualResult)
        # false
        for test_case in self.dataFalse:
            actualResult2 = unique(test_case)
            self.assertFalse(actualResult2)

def unique(s: str) -> bool:
    if s == '':
        return True
    # sử dụng dict, tức là 1 key có tần suất 2 sẽ trả về false
    char_set = {}
    for char in s:
        char_set[char] = char_set.get(char, 0) + 1
        if char_set[char] >= 2:
            return False
        # if char in char_set:
        #     return True
        # char_set[char] = True
    return True

if __name__ == "__main__":
    unt.main()  