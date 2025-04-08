
"""
Board: 0 = empty, 1 = player_1, 2 = player_2
"""
class Board:
    ROWS = 6
    COLUMNS = 7
    WINNING_CHAIN = 4
    DIRECTIONS = [[0, 1], [0, -1], [1, 1], [1, -1], [1, 0], [-1, 1], [-1, -1], [-1, 0]]

    def __init__(self):
        self.board = [[0] * self.COLUMNS] * self.ROWS

    def updateBoard(self, row, col, value):
        if (self.board[row][col] == 0 and
                (row + 1 == self.ROWS or self.board[row + 1][col] != 0)):
            self.board[row][col] = value

    def resetBoard(self):
        for row in range(self.ROWS):
            for col in range(self.COLUMNS):
                self.board[row][col] = 0

    def isWinningMove(self, row, col, value):
        for direction in self.DIRECTIONS:
            currRow = row
            currCol = col

            chain = 0
            while (0 < currRow < self.ROWS and
                   0 < currCol < self.COLUMNS and
                   self.board[currRow][currCol] == value):
                currRow += direction[0]
                currCol += direction[1]
                chain += 1

            if chain > self.WINNING_CHAIN:
                return True

        return False

