import poc_ttt_provided as provided
"""
Minimax Tic-Tac-Toe Player
"""

# import poc_ttt_gui
# import poc_ttt_provided as provided

# set timeout, as minimax can take a long time
# import codeskulptor
# codeskulptor.set_timeout(60)

# scoring values, DO NOT MODIFY!, for grader add provided.
SCORES = {provided.PLAYERX: 1,
          provided.DRAW: 0,
          provided.PLAYERO: -1}


def mm_move(board, player):
    """
    make a move on the board,
    takes the current board and which player should move next.
    returns a tuple with two elements; the first element is the score
    of the given board and the second element is the desired move as a
    tuple, (row, col)

    :param board: list
    :param player: number
    :return: tuple
    """
    if board.check_win() is not None:  # if the game is in progress
        return SCORES[board.check_win()], (-1, -1)  # return which player won. Also return an illegal move.

    #


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
