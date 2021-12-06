# Enterprise Products Confidential
import pandas as pd
import numpy as np


class BingoBoard:
    def __init__(self, raw):
        self.raw = raw
        self.board = self.populate()

    def populate(self):
        split_rows = self.raw.split("\n")
        row_dicts = {}
        for i, row in enumerate(split_rows):
            row_dicts[i] = row.split()

        board_df = pd.DataFrame(row_dicts).transpose()
        bingo_name = {0: "b", 1: "i", 2: "n", 3: "g", 4: "o"}

        board_df.rename(mapper=bingo_name, axis=1, inplace=True)

        return board_df

    def check_space(self, value):
        if value in self.board.values:
            self.find_the_value(value)

    def find_the_value(self, value):
        for col in list(self.board.columns):
            self.board[col] = self.board[col].map(
                lambda x: x + "X" if x == value else x
            )

    def check_bingo(self):
        bool_board = self.board
        for col in list(self.board.columns):
            bool_board[col] = bool_board[col].str.contains("X")

        # check_columns
        for col in list(bool_board.columns):
            if set(bool_board[col]):
                return True

        # transpose to check rows
        flipped_board = bool_board.transpose()
        for col in list(flipped_board.columns):
            if set(bool_board[col]):
                return True

        diag = np.diag(bool_board)

        self.check_diagonals(bool_board)

    @staticmethod
    def check_diagonals(board):
        diag = np.diag(board)
        print("debug")
