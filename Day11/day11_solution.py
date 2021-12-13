from utils import read_input
import numpy as np


def flash(octos: np.array, i, j):
    octos[i, j] = 0
    # up left
    if i > 0 and j > 0:
        if octos[i - 1, j - 1] in range(1, 9):
            octos[i - 1, j - 1] += 1
        else:
            return flash(octos, i - 1, j - 1)

    # directly up
    if i > 0:
        if octos[i - 1, j] in range(1, 9):
            octos[i - 1, j] += 1
        else:
            return flash(octos, i - 1, j)

    # up right
    if i > 0 and j < octos.shape[1] - 1:
        if octos[i - 1, j + 1] in range(1, 9):
            octos[i - 1, j + 1] += 1
        else:
            return flash(octos, i - 1, j + 1)

    # left
    if j > 0:
        if octos[i, j - 1] in range(1, 9):
            octos[i, j - 1] += 1
        else:
            return flash(octos, i, j - 1)

    # right
    if j < octos.shape[1] - 1:
        if octos[i, j + 1] != 9:
            octos[i, j + 1] += 1
        else:
            return flash(octos, i, j + 1)

    # down left
    if i < octos.shape[0] - 1 and j > 0:
        if octos[i + 1, j - 1] != 9:
            octos[i + 1, j - 1] += 1
        else:
            return flash(octos, i + 1, j - 1)

    # down
    if i < octos.shape[0] - 1:
        if octos[i + 1, j] != 9:
            octos[i + 1, j] += 1
        else:
            return flash(octos, i + 1, j)

    # down right
    if i < octos.shape[0] - 1 and j < octos.shape[1] - 1:
        if octos[i + 1, j + 1] != 9:
            octos[i + 1, j + 1] += 1
        else:
            return flash(octos, i + 1, j + 1)

    return octos


def octo_step(octos):
    octos = octos + 1
    for i, x in enumerate(octos):
        for j, y in enumerate(x):
            if y == 9:
                octos = flash(octos, i, j)
            print("D")

    return octos


if __name__ == "__main__":
    octopi = np.array([list(map(int, i)) for i in read_input("day11_sample_input.txt")])

    for i in range(0, 100):
        octopi = octo_step(octopi)

    print("d")
