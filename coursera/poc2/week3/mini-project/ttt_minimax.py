import functools
import poc_ttt_provided as provided

"""
Minimax Tic-Tac-Toe Player
Author: Rafeh Qazi
Link: http://www.codeskulptor.org/#user40_UjxCASn634_0.py
Course: Coursera Principles of Computing Part 2
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


def debug_helper(player):
    if player == provided.PLAYERX:
        return 'X'
    else:
        return 'O'


@functools.lru_cache(None)
def mm_move(board, player, count):
    """
    make a move on the board,
    takes the current board and which player should move next.
    returns a tuple with two elements; the first element is the score
    of the given board and the second element is the desired move as a
    tuple, (row, col)

    :param board: list
    :param player: number
    :return: tuple
    Questions: How is the stacking taking taking place within the for loop and the recursive function?
    """
    if board.check_win() is not None:  # if the game is in progress
        return SCORES[board.check_win()], (-1, -1)  # return which player won. Since board is full, return illegal move.

    new_score = (-1, (-1, -1))
    # 1. first find all the available moves from the initial position
    for idx, move_ in enumerate(board.get_empty_squares()):  # get_empty_squares method returns empty square as (row, col) tuples.
        print(board.get_empty_squares())
        print("Stack depth:", count)
        print("Current Index:", idx)
        # 2. then clone the the original board
        board_copy = board.clone()  # we do not want to store the result in the original version of the board.
        # 3. make one of the available moves with the current player
        board_copy.stuff_move(move_[0], move_[1], player)  # now the move has been made but the player needs to be switched.
        # 4. repeat this process and switch the player each time and store the winner of the game
        print("Player:", debug_helper(player))
        print("Move:", move_)
        print(board_copy)
        score, _ = mm_move(board_copy, provided.switch_player(player), count + 1)  # score each game and then swap the player
        print(score, _)  # _ returns (-1, -1) due to our base case. Also score returns the score for the winner.
        # the best possible move is found already case so now just simply go no further and return the results.
        # 5. now that you have all the possibile positions in your stack, go on and score all of them
        if score * SCORES[player] == 1:  # check if either playerO or playerX has won
            print("I won early with the following score and move")
            return score, move_

        # if score is greater than -1, replace new_score with the better score since we are only looking to maximize
        elif score * SCORES[player] > new_score[0]:
            new_score = (score, move_)
            print("\nI am in first elif:", new_score)
            print(board_copy)
        # if score is -1, or a loss for playerX, then store that score and that move.
        elif new_score[0] == -1:
            new_score = (new_score[0], move_)
            print("\nI am in second elif:", new_score)
            print(board_copy)
    # return the score and the move
    return new_score[0] * SCORES[player], new_score[1]  # we will get to this only if it is a loss for us


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


def run():
    board = provided.TTTBoard(3, False, [[provided.EMPTY, provided.EMPTY, provided.EMPTY],
                                         [provided.EMPTY, provided.EMPTY, provided.EMPTY],
                                         [provided.PLAYERX, provided.PLAYERO, provided.EMPTY]])
    # print(provided.PLAYERX, provided.PLAYERO)
    print("Answer: {0}".format(mm_move(board, provided.PLAYERX, 0)))


run()
