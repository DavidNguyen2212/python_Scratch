import pygame as pg
import ChessEngine
import os

os.chdir(r"C:\Users\DELL\Documents\Python3\Chap 16. Big game\KingChess")

WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}

"""
Khởi tạo một từ điển hình ảnh toàn cục, được gọi 1 lần duy nhất ở main
"""
def loadImages():
    pieces = ["wp", "wR", "wN", "wB", "wQ", "wK", "bp", "bR", "bN", "bB", "bQ", "bK"]
    for piece in pieces:
        IMAGES[piece] = pg.transform.scale(pg.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))


def main():
    pg.init()
    screen = pg.display.set_mode((WIDTH,HEIGHT))
    clock = pg.time.Clock()
    screen.fill(pg.Color("white"))
    gs = ChessEngine.GameState()
    validMoves = gs.getValidMoves()
    moveMade = False
    loadImages()    # Chỉ thực hiện 1 lần trước while loop
    running = True
    # Theo dõi lần click cuối cùng
    sqSelected = ()
    # Theo dõi 2 lần click
    playerClicks = []
    while running:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                running = False
            elif e.type == pg.MOUSEBUTTONDOWN:
                location = pg.mouse.get_pos()
                col = location[0] // SQ_SIZE
                row = location[1] // SQ_SIZE
                if sqSelected == (row, col):    # Người dùng nhấn trùng ô
                    sqSelected = () # Khử chọn
                    playerClicks = []   # Xóa các lần kích chuột
                else:
                    sqSelected = (row, col)
                    playerClicks.append(sqSelected)
                if len(playerClicks) == 2:
                    move = ChessEngine.Move(playerClicks[0], playerClicks[1], gs.board)
                    print(move.getChessNotation())
                    if move in validMoves:
                        gs.makeMove(move)
                        moveMade = True
                    sqSelected = () # Reset lượt click
                    playerClicks = []
            elif e.type == pg.KEYDOWN:
                if e.key == pg.K_z:     # phím z trong pygame
                    gs.undoMove()
                    moveMade = True
        
        if moveMade:
            # Chỉ sinh các nước đi hợp lệ lần nữa khi nước đi hợp lệ đã được đưa ra
            validMoves = gs.getValidMoves()
            moveMade = False    
        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        pg.display.flip()

"""
Hàm đồ họa của game
"""
def drawGameState(screen, gs):
    drawBoard(screen)
    drawPieces(screen, gs.board)

def drawBoard(screen):
    colors = [pg.Color("white"), pg.Color(57, 172, 57)]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[(r+c) % 2]    
            pg.draw.rect(screen, color, pg.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))

def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--":   # ô không rỗng
                screen.blit(IMAGES[piece], pg.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))

if __name__ == "__main__":
    main()
