"""
Lưu thông tin trạng thái hiện tại, chịu trách nhiệm cho việc ra nước đi hợp lệ từ trạng thái hiện tại.
Lưu trữ nhật ký di chuyển
"""
class GameState():
    def __init__(self):
        # Bàn cờ là ma trận 8 * 8, mỗi phần tử có 2 ký tự
        # Ký tự 1: màu đen (b), trắng (w)
        # Ký tự 2: loại quân (piece) R-Xe N-Mã B-Tượng Q-Hậu K-Vua
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"],
        ]
        self.whiteToMove = True
        self.moveLog = []