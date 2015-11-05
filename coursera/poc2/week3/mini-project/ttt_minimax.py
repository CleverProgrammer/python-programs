from poc_ttt_provided import PLAYERX, EMPTY, PLAYERO, DRAW, switch_player
"""
Minimax Tic-Tac-Toe Player
"""

# import poc_ttt_gui
# import poc_ttt_provided as provided

# set timeout, as minimax can take a long time
# import codeskulptor
# codeskulptor.set_timeout(60)

# scoring values, DO NOT MODIFY!, for grader add provided.
SCORES = {PLAYERX: 1,
          DRAW: 0,
          PLAYERO: -1}


def mm_move(board, player):
    """
    make a move on the board,

    returns a tuple with two elements; the first element is the score
    of the given board and the second element is the desired move as a
    tuple, (row, col)
    """
    # base case, the game is effectively over
    if board.check_win() is not None:
        return SCORES[board.check_win()], (-1, -1)

    # recursion(s)
    # worst possible initial values
    result = (-1, (-1, -1))
    # depth first search along the tree
    for move in board.get_empty_squares():
        copied_board = board.clone()
        copied_board.move(move[0], move[1], player)
        score, _ = mm_move(copied_board, switch_player(player))  # for grader add provided.
        # best possible choice found already
        if score * SCORES[player] == 1:
            return score, move
        # update the initial values
        elif score * SCORES[player] > result[0]:
            result = (score, move)
        elif result[0] == -1:
            result = (result[0], move)

    return result[0] * SCORES[player], result[1]


def move_wrapper(board, player, trials):
    """
    wrapper function to allow the use of the same infrastructure that was used
    for Tic-Tac-Toe (Monte Carlo method)
    """
    move = mm_move(board, player)
    assert move[1] != (-1, -1), 'returned illegal move (-1, -1)'
    return move[1]

    # test game with the console or the GUI; uncomment whichever you prefer
    # both should be commented out when you submit for testing to save time

    # play_game(move_wrapper, 1, False)
    # poc_ttt_gui.run_gui(3, provided.PLAYERO, move_wrapper, 1, False)
