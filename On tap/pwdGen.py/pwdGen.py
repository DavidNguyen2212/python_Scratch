import random
import string

LETTERS = string.ascii_letters  # CHỮ CÁI
NUMBERS = string.digits     # Chữ số
PUNCTUATION = string.punctuation    # DẤU CÂU   

# print(LETTERS)
# print(NUMBERS)
# print(PUNCTUATION)
def passwordGenerator(length: int=8):
    printable = f"{LETTERS}{NUMBERS}{PUNCTUATION}"
    printable = list(printable)     
    random.shuffle(printable)   # shuffle chỉ nhận mutable nên phải chuyển str thành list trước 

    random_password = random.choices(printable, k = length)
    random_password = ''.join(random_password)
    return random_password

def get_password_length():
    len = int(input("How long do u want your pass be: "))
    return len
def main():
    pass_len = get_password_length()
    password = passwordGenerator(pass_len)
    print("Gen pass:", password)
    
if __name__ == "__main__":
    main()