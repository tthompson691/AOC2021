# Enterprise Products Confidential
import pandas as pd
from board_class import BingoBoard


if __name__ == "__main__":
    # read input
    with open("day4_input1.txt", "r") as f:
        calls = f.read().split(",")

    with open("day4_input2.txt", "r") as f:
        boards = f.read().split("\n\n")

    all_boards = [BingoBoard(board) for board in boards]

    for board in all_boards:
        board.check_space("76")
        board.check_bingo()

    print("debug")
