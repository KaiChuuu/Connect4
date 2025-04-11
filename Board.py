
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
        self.board = [[0 for _ in range(self.COLUMNS)] for _ in range(self.ROWS)]

    def update_board(self, row, col, value):
        if (self.board[row][col] == 0 and
                (row + 1 == self.ROWS or self.board[row + 1][col] != 0)):
            self.board[row][col] = value

    def reset_board(self):
        for row in range(self.ROWS):
            for col in range(self.COLUMNS):
                self.board[row][col] = 0

    def is_winning_move(self, row, col, value):
        for direction in self.DIRECTIONS:
            fwd_row = row
            fwd_col = col

            chain = 0
            while (0 <= fwd_row < self.ROWS and
                   0 <= fwd_col < self.COLUMNS and
                   self.board[fwd_row][fwd_col] == value):
                fwd_row += direction[0]
                fwd_col += direction[1]
                chain += 1

            bwd_row = row
            bwd_col = col
            while (0 <= bwd_row < self.ROWS and
                   0 <= bwd_col < self.COLUMNS and
                   self.board[bwd_row][bwd_col] == value):
                bwd_row -= direction[0]
                bwd_col -= direction[1]
                chain += 1

            if chain - 1 >= self.WINNING_CHAIN:
                return True

        return False

    def print_board(self):
        for row in self.board:
            print(' '.join(str(slot) for slot in row))
        print()