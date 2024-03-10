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
            ["--", "--", "--", "bp", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"],
        ]
        self.whiteToMove = True
        # Thuộc tính phụ trách Undo
        self.moveLog = []   

    # Lấy một bước đi làm tham số, thực thi nó (chưa tính đến Nhập thành-castling và bắt tốt qua đường - enpassant)
    def makeMove(self, move):
        self.board[move.startRow][move.startCol] = "--"
        self.board[move.endRow][move.endCol] = move.pieceMoved
        self.moveLog.append(move)
        self.whiteToMove = not self.whiteToMove # Đổi lượt đi

    """
    Undo bước đi vừa thực hiện
    """
    def undoMove(self):
        if len(self.moveLog) != 0:
            move = self.moveLog.pop()
            self.board[move.startRow][move.startCol] = move.pieceMoved
            self.board[move.endRow][move.endCol] = move.pieceCaptured
            self.whiteToMove = not self.whiteToMove    

    """
    Kiểm tra nước đi có hợp lệ không
    """
    def getValidMoves(self):
        return self.getAllPossibleMoves()   # chưa quan tâm đến nước Chiếu (check)
    def getAllPossibleMoves(self):
        moves = []
        for r in range(len(self.board)):    # đi qua từng dòng
            for c in range(len(self.board[r])): # duyệt dòng đó
                turn = self.board[r][c][0]
                if (turn == 'w' and self.whiteToMove) or (turn == 'b' and not self.whiteToMove):
                    piece = self.board[r][c][1]
                    if piece == 'p':
                        self.getPawnMoves(r, c, moves)
                    elif piece == 'R':
                        self.getRookMoves(r, c, moves)
        return moves
                    

    def getPawnMoves(self, r, c, moves):
        if self.whiteToMove:
            if self.board[r-1][c] == "--":
                moves.append(Move((r,c), (r-1,c), self.board))
                if r == 6 and self.board[r-2][c] == "--":   # Tốt xuất phát & 2 ô
                    moves.append(Move((r,c), (r-2,c), self.board))
            if c - 1 >= 0:  # test để bắt bên trái
                if self.board[r-1][c-1][0] == 'b': 
                    moves.append(Move((r,c), (r-1,c-1), self.board))
            if c + 1 <= 7:   # test để bắt bên phải
                if self.board[r-1][c+1][0] == 'b':
                    moves.append(Move((r,c), (r-1, c+1), self.board))
        
        else:   # tương tự với tốt đen
            if self.board[r+1][c] == "--":
                moves.append(Move((r,c), (r+1, c), self.board))
                if r == 2 and self.board[r+2][c] == "--":
                    moves.append(Move((r,c), (r+2,c), self.board))
            if c - 1 >= 0:
                if self.board[r+1][c-1][0] == "w":
                    moves.append(Move((r,c), (r+1, c-1), self.board))
            if c + 1 <= 7:
                if self.board[r+1][c+1][0] == "w":
                    moves.append(Move((r,c), (r+1, c+1), self.board))  

    def getRookMoves(self, r, c, moves):
        pass

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
        # Như một hash function
        self.moveID = self.startRow * 1000 + self.startCol * 100 + self.endRow * 10 + self.endCol   
        print(self.moveID)

    """Override toán tử ="""
    def __eq__(self, other) -> bool:
        if isinstance(other, Move):
            return self.moveID == other.moveID
        return False

    def getChessNotation(self):
        return self.getRankFile(self.startRow, self.startCol) + " --> " + self.getRankFile(self.endRow, self.endCol)
    def getRankFile(self, r, c):
        return self.colstoFiles[c] + self.rowstoRanks[r]