
"""
Board: 0 = empty, 1 = player_1, 2 = player_2
"""
class Board:
    WINNING_CHAIN = 4
    DIRECTIONS = [[0, 1], [0, -1], [1, 1], [1, -1], [1, 0], [-1, 1], [-1, -1], [-1, 0]]

    def __init__(self, rows, columns, winning_chain):
        self.ROWS = rows
        self.COLUMNS = columns
        self.WINNING_CHAIN = winning_chain
        self.board = [[0] * self.COLUMNS] * self.ROWS

    def update_board(self, row, col, value):
        # just pass in col, and find row thats empty (if possible)
        if (self.board[row][col] == 0 and
                (row + 1 == self.ROWS or self.board[row + 1][col] != 0)):
            self.board[row][col] = value

    def reset_board(self):
        for row in range(self.ROWS):
            for col in range(self.COLUMNS):
                self.board[row][col] = 0

    def is_winning_move(self, row, col, value):
        for direction in self.DIRECTIONS:
            curr_row = row
            curr_col = col

            chain = 0
            while (0 < curr_row < self.ROWS and
                   0 < curr_col < self.COLUMNS and
                   self.board[curr_row][curr_col] == value):
                curr_row += direction[0]
                curr_col += direction[1]
                chain += 1

            if chain > self.WINNING_CHAIN:
                return True

        return False

