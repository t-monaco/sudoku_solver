import pprint
import numpy as np

grid = [
    [5, 0, 0, 0, 8, 1, 2, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 4, 0, 3, 9, 0, 0],
    [0, 6, 4, 0, 0, 0, 0, 8, 0],
    [0, 7, 0, 0, 0, 0, 0, 0, 3],
    [0, 0, 0, 2, 0, 0, 7, 0, 0],
    [0, 3, 0, 0, 0, 0, 0, 9, 6],
    [9, 0, 0, 0, 3, 0, 0, 0, 4],
    [0, 0, 0, 0, 1, 5, 0, 0, 0]
]


def possible(y, x, n):
    global grid
    for i in range(0, 9):
        if grid[y][i] == n:
            return False
    for i in range(0, 9):
        if grid[i][x] == n:
            return False
    y0 = (y // 3) * 3
    x0 = (x // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if grid[y0 + i][x0 + j] == n:
                return False
    return True


def solve():
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1, 10):
                    if possible(y, x, n):
                        grid[y][x] = n
                        solve()
                        grid[y][x] = 0
                return
    # print(*grid, sep='\n')
    print_board(grid)
    input('More?')


def print_board(bo):
    """
    prints the board
    :param bo: 2d List of ints
    :return: None
    """
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j], end="\n")
            else:
                print(str(bo[i][j]) + " ", end="")


solve()
