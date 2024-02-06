# Bản chất của lệnh này, nó import module + những câu lệnh cấp cao (không thụt dòng)
# Do đó nếu muốn bảo vệ các lệnh trong module phụ, thì cần if name main
from module_phu import func1    

print("Welcome to main program", __name__)
