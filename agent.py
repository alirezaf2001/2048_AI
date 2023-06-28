import random
from copy import deepcopy
from game import Game
from time import sleep
import numpy as np

def recursive(game,depth):
    if depth == 5:
        return fittness(game), 0
    else:
        games = []
        scores = []
        for i in range(4):
            games.append(deepcopy(game))
        move = []
        move.append(games[0].move_up())
        move.append(games[1].move_down())
        move.append(games[2].move_left())
        move.append(games[3].move_right())
        for i in range(4):
            if move[i]:
                scores.append(recursive(games[i], depth+1))
            else:
                scores.append((0, 0))
        max_score = max(scores, key=lambda x: x[0])
        maxindx = scores.index(max_score)
        return max_score[0] + fittness(game), maxindx





def fittness(game):
    score = game.total_add

    score += game.board[0][0] * 16
    score += game.board[0][1] * 15
    score += game.board[0][2] * 14
    score += game.board[0][3] * 13
    score += game.board[1][0] * 9
    score += game.board[1][1] * 10
    score += game.board[1][2] * 11
    score += game.board[1][3] * 12


    for row in game.board:
        for i in range(3):
            if row[i] == row[i+1]:
                score += row[i]
    for column in game.board.T:
        for i in range(3):
            if column[i] == column[i+1]:
                score += column[i]
    return score

def play_random(board):
    game = Game(deepcopy(board))
    # arr = []
    # for i in range(4):
    #     arr.append(deepcopy(game))
    #
    # arr[0].move_up()
    # arr[1].move_down()
    # arr[2].move_left()
    # arr[3].move_right()
    # scores = []
    # for i in range(4):
    #     scores.append(fittness(arr[i]))

    # maxind = 4
    # max = 0
    # for i in range(4):
    #     if scores[i]> max:
    #         max = scores[i]
    #         maxind = i
    score, i = recursive(game, 0)
    print(score)
    # sleep(0.05)
    if i == 0:
        return 'w'
    elif i == 1:
        return 's'
    elif i == 2:
        return 'a'
    elif i == 3:
        return 'd'

    choice = random.choice(['w', 's', 'a', 'd'])
    return choice
