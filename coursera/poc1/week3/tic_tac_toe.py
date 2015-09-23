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
    for i in range(x):
        move = random.randrange(1, 9)
        pass


def mc_update(scores, board, player):
    '''
    his function takes a grid of scores (a list of lists) with the same dimensions as the Tic-Tac-Toe board,
    a board from a completed game, and which player the machine player is. The function should score the
    completed board and update the scores grid. As the function updates the scores grid directly,
    it does not return anything.
    '''


class Tic_Tac_Toe(unittest.TestCase):

    def test_function_name(self):
        # self.assertEqual(function_name([0, 0, 2, 2]), [4, 0, 0, 0])
        pass


suite = unittest.TestLoader().loadTestsFromTestCase(Tic_Tac_Toe)
unittest.TextTestRunner(verbosity=2).run(suite)
