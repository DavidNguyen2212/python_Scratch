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
        # Thuộc tính phụ trách Undo
        self.moveLog = []   

    def makeMove(self, move):
        self.board[move.startRow][move.startCol] = "--"
        self.board[move.endRow][move.endCol] = move.pieceMoved
        self.moveLog.append(move)
        self.whiteToMove = not self.whiteToMove # Đổi lượt đi

class Move:
    # Ánh xạ key:value
    rankstoRows = {"1":7, "2":6, "3":5, "4":4, "5":3, "6":2, "7":1, "8":0}
    rowstoRanks = {v:k for k,v in rankstoRows.items()}
    filestoCols = {"a":0, "b":1, "c":2, "d":3, "e":4, "f":5, "g":6, "h":7}
    colstoFiles = {v:k for k,v in filestoCols.items()}

    def __init__(self, startSq, endSq, board):
        self.startRow = startSq[0]
        self.startCol = startSq[1]
        self.endRow = endSq[0]
        self.endCol = endSq[1]
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]

    def getChessNotation(self):
        return self.getRankFile(self.startRow, self.startCol) + " --> " + self.getRankFile(self.endRow, self.endCol)
    def getRankFile(self, r, c):
        return self.colstoFiles[c] + self.rowstoRanks[r]