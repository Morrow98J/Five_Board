# Author: Jacob Morrow
# Date: 08/13/2020
# Description: a class called FiveBoard that represents the board for a two-player game that is like tic-tac-toe, but on
# a larger scale. Instead of a 3x3 board, it is played on a 15x15 board, and instead of 3 in a row, each player is
# trying to get 5 of their pieces in a row. The row of pieces can be vertical, horizontal, or diagonal.


class FiveBoard:
    """FiveBoard: represents the board for a two-player game  like tic-tac-toe, but 15x15 and 5 in a row to win"""

    def __init__(self):
        """A representation of the board and the current state"""
        self._board = [["_"] * 15 for i in range(15)]
        self._current_state = "UNFINISHED"

    def make_move(self, r, c, ox):
        """Three parameters: a row and a column (in that order) where each is an integer in the range 0-14, and either
        'x' or 'o' to indicate the player who is making the move"""
        if self._current_state != "UNFINISHED" or self._board[r][c] != "_":
            return False
        else:
            self._board[r][c] = ox
            if self.win_row(ox) or self.win_col(ox) or self.win_angle(ox):
                self._current_state = ox.upper() + "_WON"
            if self.check_empty():
                self._current_state = "DRAW"
            return True

    def win_col(self, ox):
        """Win condition for 5 x's or o's aligned in a column on the board"""
        col_board = list(zip(*self._board))
        for col in col_board:
            if col.count(ox) >= 5:
                return True
        return False

    def win_row(self, ox):
        """Win condition for 5 x's or o's aligned in a row on the board"""
        for row in self._board:
            if row.count(ox) >= 5:
                return True
        return False

    def win_angle(self, ox):
        """Win condition for 5 x's or o's aligned in either diagonal, with angle_board being from top left to bottom
        right and angle_reverse being from top right to bottom left on the board"""
        board_reverse = [row[::-1] for row in self._board]  # Reversing the board to use the same list comprehension
        angle_board = [[self._board[c - r][r] for r in range(15) if 0 <= c - r < 15] for c in range(28)]
        angle_reverse = [[board_reverse[c - r][r] for r in range(15) if 0 <= c - r < 15] for c in range(28)]
        for angle in angle_reverse + angle_board:
            if angle.count(ox) >= 5:
                return True
        return False

    def get_current_state(self):
        """Returns _current_state"""
        return self._current_state

    def get_board(self):
        """Prints the 15x15 board"""
        for row in self._board:
            print(row)

    def check_empty(self):
        """Returns True if all positions are filled"""
        for row in self._board:
            for i in row:
                if i == "_":
                    return False
        return True


'''board = FiveBoard()
board.make_move(1, 5, 'x')
board.make_move(2, 4, 'x')
board.make_move(3, 3, 'x')
board.make_move(4, 2, 'x')
board.make_move(5, 1, 'x')
print(board.get_current_state())
print(board.get_board())'''
# Test code for top right to bottom left X_WON
