from utils import read_input
import numpy as np


def flash(octos, i, j):
    nu = nd = nl = nr = None
    if i > 0:
        nu = (i - 1, j)
    if i < octos.shape[0] - 1:
        nd = (i + 1, j)
    if j > 0:
        nl = (i, j - 1)
    if j < octos.shape[1] - 1:
        nr = (i, j + 1)


def octo_step(octos):
    octos = octos + 1
    while np.any(octos == 9):
        for i, x in enumerate(octos):
            for j, y in enumerate(x):
                if y == 9:
                    flash(octos, i, j)
                print("D")


if __name__ == "__main__":
    octopi = np.array([list(map(int, i)) for i in read_input("day11_sample_input.txt")])

    octo_step(octopi)

    print("d")
