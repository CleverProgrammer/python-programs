"""
Author: Rafeh Qazi
Monte Carlo Tic-Tac-Toe Player
Date: 09/27/2015
Link for Testing: http://www.codeskulptor.org/#user40_b7MoftHwHl_0.py
Link for Program: http://www.codeskulptor.org/#user40_rBVyJW3zdp_11.py
"""
import random
import poc_simpletest
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 200        # Number of trials to run
SCORE_CURRENT = 1.0  # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player

# ------------------------ FUNCTIONS --------------------------- #


def mc_trial(board, player):
    '''
    This function takes a current board and the next player to move.
    The function should play a game starting with the given player by making random moves,
    alternating between players. The function should return when the game is over.
    '''
    in_progress = lambda: not board.check_win()
    while in_progress():
        row, col = random.choice(board.get_empty_squares())
        board.move(row, col, player)
        provided.switch_player(player)


def mc_update_scores(scores, board, player):
    '''
    Update the game score
    '''
    # Scores probably looks like: [ [0,0,0], [0,0,0], [0,0,0] ]

    if board.check_win() == provided.DRAW:
        return
    elif player == board.check_win():
        sign = 1
    elif player != board.check_win():
        sign = -1
    for row in range(len(scores[0])):
        for col in range(len(scores[0])):
            if board.square(row, col) == player:
                scores[row][col] += sign * SCORE_CURRENT
            elif board.square(row, col) == provided.switch_player(player):
                scores[row][col] -= sign * SCORE_OTHER
    return scores


def get_best_move(board, scores):
    '''
    Take board and scores. Return a randomly picked tuple of best moves
    '''
    nrow = ncol = board.get_dim()
    max_value = 0
    score_index = {}
    for row in range(len(scores)):
        for col in range(len(scores[row])):
            if (row, col) not in board.get_empty_squares():
                continue
            score = scores[row][col]
            if score not in score_index:
                score_index[score] = [(row, col)]
            else:
                score_index[score].append((row, col))
    best_score = max(score_index)
    return random.choice(score_index[best_score])


def mc_move(board, player, trials):
    '''
    This function takes a current board, 
    which player the machine player is, 
    and the number of trials to run. 
    The function should use the Monte Carlo simulation 
    described above to return a move for the 
    machine player in the form of a (row, column) tuple. 
    Be sure to use the other functions you have written!
    '''
    scores = [[0] * board.get_dim() for _ in range(board.get_dim())]
    i = 0
    best_move = None
    while i < trials:
        board_copy = board.clone()
        mc_trial(board_copy, player)
        new_scores = mc_update_scores(scores, board_copy, trials)
        best_move = get_best_move(board, new_scores)
        i += 1
    return best_move

# provided.play_game(mc_move, NTRIALS, False)
# poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
