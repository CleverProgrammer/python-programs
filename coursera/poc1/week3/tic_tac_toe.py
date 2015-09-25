#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-09-23 13:32:01
# @Author  : Rafeh Qazi (rafehqazi1@gmail.com)
# @Link    :

import unittest


"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 1         # Number of trials to run
SCORE_CURRENT = 1.0  # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player

# Add your functions here.


def mc_trial(board, player):
    '''
    This function takes a current board and the next player to move.
    The function should play a game starting with the given player by making random moves,
    alternating between players. The function should return when the game is over.
    The modified board will contain the state of the game, so the function does not return anything.
    In other words, the function should modify the board input.
    '''
    in_progress = lambda: not board.check_win()
    while in_progress():
        row, col = random.choice(board.get_empty_squares())
        board.move(row, col, player)
        provided.switch_player(player)


def mc_update_scores(scores, board, player):
    '''
    This function takes a grid of scores (a list of lists) with the same dimensions as the Tic-Tac-Toe board,
    a board from a completed game, and which player the machine player is. The function should score the
    completed board and update the scores grid. As the function updates the scores grid directly,
    it does not return anything.
    '''
    # Scores probably looks like: [ [0,0,0], [0,0,0], [0,0,0] ]
    if player == board.check_win():
        sign = 1
    elif player != board.check_win():
        sign = -1
    elif board.check_win() == provided.DRAW:
        return
    for row in scores:
        for col in row:
            if board.square(row, col) == player:
                scores[row][col] += sign * SCORE_CURRENT
            if board.square(row, col) != provided.EMPTY:
                scores[row][col] -= sign * SCORE_OTHER
    print(scores)


class TTT(unittest.TestCase):

    def test_function_name(self):
        # self.assertEqual(function_name([0, 0, 2, 2]), [4, 0, 0, 0])
        pass


suite = unittest.TestLoader().loadTestsFromTestCase(TTT)
unittest.TextTestRunner(verbosity=2).run(suite)
