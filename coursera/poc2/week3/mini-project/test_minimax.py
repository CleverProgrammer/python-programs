import unittest

from poc_ttt_provided import TTTBoard
from ttt_minimax import mm_move
from poc_ttt_provided import DRAW, EMPTY, PLAYERO, PLAYERX


class TestTTTMinimax(unittest.TestCase):
    def setUp(self):
        pass

    def test_move_it(self):
        board = TTTBoard(3, False,
                         [[PLAYERO, PLAYERX, PLAYERX], [PLAYERO, PLAYERX, PLAYERO], [PLAYERX, PLAYERO, PLAYERX]])
        self.assertIsInstance(board, TTTBoard)  # assert board is an instance of TTTBoard class
        self.assertIs(type(mm_move(board, PLAYERX)), tuple)  # assert mm_move function returns a tuple
        score, move = mm_move(board, PLAYERX)  # mm_move returns a score, and a move value
        self.assertIs(type(score), int)  # assert score is an int
        self.assertIs(type(move), tuple)  # assert move is a tuple
        self.assertEqual(mm_move(board, PLAYERX), (1, (-1, -1)))  # return an illegal move since the game is over.
        board = TTTBoard(3, False,
                         [[PLAYERO, PLAYERX, PLAYERX], [PLAYERX, PLAYERO, PLAYERO], [PLAYERO, PLAYERX, PLAYERX]])
        self.assertEqual(mm_move(board, DRAW), (0, (-1, -1)))
        board = TTTBoard(3, False,
                         [[PLAYERO, PLAYERX, PLAYERX], [PLAYERO, PLAYERX, PLAYERO], [PLAYERO, PLAYERO, PLAYERX]])
        self.assertEqual(mm_move(board, PLAYERO), (-1, (-1, -1)))

    def test_won_it(self):
        board = TTTBoard(3, False,
                         [[PLAYERX, PLAYERX, PLAYERO], [PLAYERO, PLAYERX, PLAYERX], [PLAYERO, EMPTY, PLAYERO]])
        self.assertEqual(mm_move(board, PLAYERX), (1, (2, 1)))
        board = TTTBoard(2, False, [[EMPTY, EMPTY], [EMPTY, EMPTY]])
        self.assertEqual(mm_move(board, PLAYERX), (1, (0, 0)))

    def test_draw(self):
        board = TTTBoard(3, False, [[EMPTY, EMPTY, PLAYERX], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]])
        self.assertEqual(mm_move(board, PLAYERO), (0, (1, 1)))
        board = TTTBoard(3, False, [[PLAYERX, EMPTY, EMPTY], [PLAYERO, PLAYERO, EMPTY], [EMPTY, PLAYERX, EMPTY]])
        self.assertEqual(mm_move(board, PLAYERX), (0, (1, 2)))
        board = TTTBoard(3, False, [[EMPTY, EMPTY, PLAYERX], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]])
        self.assertEqual(mm_move(board, PLAYERO), (0, (1, 1)))

    def test_lost_it(self):
        board = TTTBoard(3, False, [[PLAYERX, PLAYERX, PLAYERO], [EMPTY, PLAYERX, PLAYERX], [PLAYERO, EMPTY, PLAYERO]])
        self.assertEqual(mm_move(board, PLAYERO), (-1, (2, 1)))
        board = TTTBoard(3, False, [[PLAYERX, PLAYERX, PLAYERO], [EMPTY, PLAYERX, PLAYERX], [PLAYERO, EMPTY, PLAYERO]])
        self.assertEqual(mm_move(board, PLAYERO), (-1, (2, 1)))


if __name__ == '__main__':
    unittest.main()
