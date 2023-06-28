import numpy as np
import random


# Shift Left
def shift_left(array):
    total_add = 0
    move = False
    for i in range(1, 4):
        if array[i] != 0:
            for j in range(i - 1, -1, -1):
                if j == 0:
                    if array[j] == 0:
                        array[j] = array[i]
                        array[i] = 0
                        move = True
                        break
                elif array[j - 1] != 0:
                    if array[j] == 0:
                        array[j] = array[i]
                        array[i] = 0
                        move = True
                        break
    for i in range(3):
        if array[i] == array[i+1] and array[i] != 0:
            array[i] += array[i+1]
            total_add += array[i]
            array[i+1] = 0
            move = True
    for i in range(1, 4):
        if array[i] != 0:
            for j in range(i - 1, -1, -1):
                if j == 0:
                    if array[j] == 0:
                        array[j] = array[i]
                        array[i] = 0


                        break
                elif array[j - 1] != 0:
                    if array[j] == 0:
                        array[j] = array[i]
                        array[i] = 0
                        break
    return move, total_add


# Shift Right
def shift_right(array):
    total_add = 0
    move = False
    for i in range(3, -1, -1):
        if array[i] != 0:
            for j in range(i + 1, 4):
                if j == 3:
                    if array[j] == 0:
                        array[j] = array[i]
                        array[i] = 0
                        move = True
                        break
                elif array[(j + 1) % 4] != 0:
                    if array[j] == 0:
                        array[j] = array[i]
                        array[i] = 0
                        move = True
                        break

    for i in range(3, 0, -1):
        if array[i] == array[i-1] and array[i] != 0:
            array[i] += array[i-1]
            total_add += array[i]
            array[i-1] = 0
            move = True
    for i in range(3, -1, -1):
        if array[i] != 0:
            for j in range(i + 1, 4):
                if j == 3:
                    if array[j] == 0:
                        array[j] = array[i]
                        array[i] = 0
                        break
                elif array[(j + 1) % 4] != 0:
                    if array[j] == 0:
                        array[j] = array[i]
                        array[i] = 0
                        break
    return move, total_add

# GAME CLASS
class Game:
    # Initial board
    def __init__(self, board=np.empty(0)):
        if board.shape == (0,):
            self.board = np.zeros(shape=(4, 4), dtype=np.int32)
            rows = random.sample(range(0, 4), 2)
            cols = (random.randint(0, 3), random.randint(0, 3))
            self.board[rows[0], cols[0]] = 2
            self.board[rows[1], cols[1]] = 2
        else:
            self.board = board
        self.total_add = 0

    def info(self):
        count = np.count_nonzero(self.board)
        return count

    # New Cell
    def new_cell(self):
        zeros = np.where(self.board == 0)
        pos = random.choice(range(len(zeros[0])))
        self.board[zeros[0][pos], zeros[1][pos]] = random.choice([2, 4])
    # Define Movements
    def move_up(self):
        move = False
        for column in self.board.T:
            res = shift_left(column)
            self.total_add += res[1]
            if res[0]:
                move = res[0]
        return move

    def move_down(self):
        move = False
        for column in self.board.T:
            res = shift_right(column)
            self.total_add += res[1]
            if res[0]:
                move = res[0]
        return move

    def move_left(self):
        move = False
        for row in self.board:
            res = shift_left(row)
            self.total_add += res[1]
            if res[0]:
                move = res[0]
        return move
    def move_right(self):
        move = False
        for row in self.board:
            res = shift_right(row)
            self.total_add += res[1]
            if res[0]:
                move = res[0]
        return move

    # Print Board
    def print_board(self):
        print(self.board)

    # Return Board
    def get_board(self):
        return self.board

