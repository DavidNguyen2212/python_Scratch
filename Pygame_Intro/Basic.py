# Đưa thư viện vào
import pygame, sys
from pygame.locals import *     # ???

# Khởi đầu
pygame.init()

# Màu trong pygame theo RGB
GRAY = (100, 100, 100)
BLUE = (0, 0, 255)

# Đối tượng hình chữ nhật
myRect = pygame.Rect(50, 50, 100, 100)  # left, top, width, height
print(myRect.top)
# Tạo giao diện
DISPLAYSURF = pygame.display.set_mode((500, 400))   # tuple px * px
pygame.display.set_caption("Hello")     # Đặt tên cửa sổ
while True:
    for event in pygame.event.get():    # lấy sự kiện
        if event.type == QUIT:          # QUIT là constant var trong locals
            pygame.quit()
            sys.exit()
    pygame.display.update()

