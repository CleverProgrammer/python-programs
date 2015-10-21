#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-09-22 07:45:56
# @Author  : Rafeh Qazi (rafehqazi1@gmail.com)
# @Link    : http://www.codeskulptor.org/#poc_nim_mc_template.py
# Shortcuts: |Multiple_cursor: cmd+ctrl+g| |Build: cmd+b| |Doc: ctrl+alt+d|
import unittest
import random

MAX_REMOVE = 3
TRIALS = 10000


def evaluate_position(num_items):
    """
    Monte Carlo evalation method for Nim
    """
    total_wins = -1
    best_move = 0
    for first_move in range(1, MAX_REMOVE + 1):
        wins = 0
        for _ in range(TRIALS):
            total = first_move
            computer_move = True
            while total < num_items:
                total += random.randrange(1, MAX_REMOVE + 1)
                computer_move = not computer_move
            if computer_move:
                wins += 1
        if wins > total_wins:
            total_wins = wins
            best_move = first_move
    return best_move


def play_game(start_items):
    """
    Play game of Nim against Monte Carlo bot
    """

    current_items = start_items
    print("Starting game with value", current_items)
    while True:
        comp_move = evaluate_position(current_items)
        current_items -= comp_move
        print("Computer choose", comp_move,
              ", current value is", current_items)
        if current_items <= 0:
            print("Computer wins")
            break
        player_move = int((input("Enter your current move:\n")))
        current_items -= player_move
        print("Player choose", player_move,
              ", current value is", current_items)
        if current_items <= 0:
            print("Player wins")
            break

play_game(21)


class ClassName(unittest.TestCase):

    def test_function_name(self):
        # self.assertEqual(function_name([0, 0, 2, 2]), [4, 0, 0, 0])
        pass

suite = unittest.TestLoader().loadTestsFromTestCase(ClassName)
unittest.TextTestRunner(verbosity=2).run(suite)
