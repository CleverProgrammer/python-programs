import unittest
from fifteen import Puzzle


class TestFifteen(unittest.TestCase):
    def test_lower_row_invariant(self):
        fifteen = Puzzle(4, 4)
        fifteen._grid[0][0], fifteen._grid[2][1] = fifteen._grid[2][1], \
                                                   fifteen._grid[0][0]
        self.assertEqual(fifteen.lower_row_invariant(2, 1), True)
        # now let's create a situation where the invariant does NOT hold
        fifteen = Puzzle(4, 4)
        fifteen._grid[0][0], fifteen._grid[2][1] = fifteen._grid[2][1], \
                                                   fifteen._grid[0][0]
        fifteen._grid[0][1], fifteen._grid[3][2] = fifteen._grid[3][2], \
                                                   fifteen._grid[0][1]
        self.assertEqual(fifteen.lower_row_invariant(2, 1), False)
        # now let's check if the invariant holds in the starting postition
        fifteen = Puzzle(4, 4)
        self.assertEqual(fifteen.lower_row_invariant(0, 0), True)
        # now let's create a situation where the invariant does NOT hold
        fifteen = Puzzle(4, 4)
        fifteen._grid[0][1], fifteen._grid[0][2] = fifteen._grid[0][2], \
                                                   fifteen._grid[0][1]
        self.assertEqual(fifteen.lower_row_invariant(0, 0), False)

    def test_solve_interior_tile(self):
        # 1. lower_row_invariant(i, j) == True
        # 2. solve_interior_tile(i, j)
        # 3. lower_row_invariant(i, j-1) == True
        fifteen = Puzzle(4, 4)
        fifteen._grid[0][0] = 4
        fifteen._grid[0][1] = 13
        fifteen._grid[0][2] = 1
        fifteen._grid[0][3] = 3
        fifteen._grid[1][0] = 5
        fifteen._grid[1][1] = 10
        fifteen._grid[1][2] = 2
        fifteen._grid[1][3] = 7
        fifteen._grid[2][0] = 8
        fifteen._grid[2][1] = 12
        fifteen._grid[2][2] = 6
        fifteen._grid[2][3] = 11
        fifteen._grid[3][0] = 9
        fifteen._grid[3][1] = 0
        fifteen._grid[3][2] = 14
        fifteen._grid[3][3] = 15
        # step 1
        self.assertEqual(fifteen.lower_row_invariant(3, 1), True)
        self.assertEqual(fifteen.lower_row_invariant(0, 0), False)
        self.assertEqual(fifteen.lower_row_invariant(0, 1), False)
        self.assertEqual(fifteen.lower_row_invariant(0, 2), False)
        self.assertEqual(fifteen.lower_row_invariant(0, 3), False)
        self.assertEqual(fifteen.lower_row_invariant(1, 0), False)
        self.assertEqual(fifteen.lower_row_invariant(1, 1), False)
        self.assertEqual(fifteen.lower_row_invariant(1, 2), False)
        self.assertEqual(fifteen.lower_row_invariant(1, 3), False)
        self.assertEqual(fifteen.lower_row_invariant(2, 0), False)
        self.assertEqual(fifteen.lower_row_invariant(2, 1), False)
        self.assertEqual(fifteen.lower_row_invariant(2, 2), False)
        self.assertEqual(fifteen.lower_row_invariant(2, 3), False)
        self.assertEqual(fifteen.lower_row_invariant(3, 0), False)
        self.assertEqual(fifteen.lower_row_invariant(3, 2), False)
        self.assertEqual(fifteen.lower_row_invariant(3, 3), False)
        # step 2
        # print('========SOLVE WHEN IT IS ABOVE=========')
        # SOLVE WHEN IT IS ABOVE AND TO THE LEFT
        # print(fifteen)
        fifteen.solve_interior_tile(3, 1)
        # print(fifteen)
        # step 3
        self.assertEqual(fifteen.lower_row_invariant(3, 0), True)
        # print('========END SOLVE WHEN IT IS ABOVE=========\n')
        # SOLVE WHEN IT IS DIRECTLY ABOVE
        # # # # print('========SOLVE WHEN IT IS ABOVE AND LEFT=========')
        fifteen = Puzzle(4, 4)
        fifteen._grid[0][0] = 14
        fifteen._grid[3][2] = 0
        # # # # print(fifteen)
        fifteen.solve_interior_tile(3, 2)
        # # # # print(fifteen)
        solved_through_strings = Puzzle(4, 4)
        solved_through_strings._grid[0][0] = 14
        solved_through_strings._grid[3][2] = 0
        solved_through_strings.update_puzzle('uuulldrruldrulddrulddruld')
        for val1, val2 in zip(fifteen._grid, solved_through_strings._grid):
            assert val1 == val2
        # # # # print(solved_through_strings)
        # # # # print('should be same as above:\n', fifteen)
        # # # # print('========END SOLVE WHEN IT IS ABOVE AND LEFT=========\n')
        # # # # print('========SOLVE WHEN IT IS ABOVE AND RIGHT=========')
        fifteen = Puzzle(4, 4)
        fifteen._grid[0][0] = 3
        fifteen._grid[0][-1] = 13
        fifteen._grid[3][1] = 0
        # # # # print(fifteen)
        fifteen.solve_interior_tile(3, 1)
        # # # # print(fifteen)
        # # # # print('========END SOLVE WHEN IT IS ABOVE AND RIGHT=========\n')
        # # # print('========SOLVE SAME ROW ONE LEFT=========')
        fifteen = Puzzle(4, 4)
        fifteen._grid[2][1] = 10
        fifteen._grid[2][2] = 0
        fifteen._grid[0][0] = 9
        # # # print(fifteen)
        fifteen.solve_interior_tile(2, 2)
        # # # print(fifteen)
        # # # print('========END SOLVE SAME ROW ONE LEFT=========\n')
        # # # print('========SOLVE WHEN IT IS IN THE SAME ROW=========')
        fifteen = Puzzle(4, 4)
        fifteen._grid[2][1] = 11
        fifteen._grid[2][-1] = 0
        fifteen._grid[0][0] = 9
        # # # print(fifteen)
        fifteen.solve_interior_tile(2, 3)
        # # # print(fifteen)
        # # # print('========END SOLVE WHEN IT IS IN THE SAME ROW=========\n')

    def test_helper_solve_interior(self):
        fifteen = Puzzle(4, 4, [[4, 13, 1, 3],
                                [5, 10, 2, 7],
                                [8, 12, 6, 11],
                                [9, 0, 14, 15]]
                         )
        # print('========SOLVE WHEN IT IS ABOVE=========')
        # print(fifteen)
        # I want 10 moved
        computed = fifteen.helper_solve_interior(target_solved_row=2, target_solved_col=2,
                                                 zero_row=3, zero_col=1,
                                                 solved_val_row=0, solved_val_col=1)
        self.assertEqual(computed, 'uulddruld')
        # self.assertEqual(fifteen.lower_row_invariant(3, 0), True)
        # print(fifteen)
        # print('========END SOLVE WHEN IT IS ABOVE=========\n')

        fifteen = Puzzle(4, 4, [[4, 13, 1, 3],
                                [5, 10, 2, 7],
                                [8, 12, 6, 11],
                                [9, 0, 14, 15]]
                         )
        # print('========SOLVE WHEN IT IS NOT ABOVE=========')
        # print(fifteen)
        # I want 3 moved
        computed = fifteen.helper_solve_interior(0, 3, zero_row=3, zero_col=1,
                                                 solved_val_row=0, solved_val_col=1)
        # self.assertEqual(fifteen.lower_row_invariant(3, 0), True)
        # print(fifteen)
        # print('========END SOLVE WHEN IT IS NOT ABOVE=========\n')

    def test_solve_col0_tile(self):
        # # print('========SOLVE TILE IN COLUMN 0=========')
        fifteen = Puzzle(4, 4)
        fifteen._grid[3][0] = 0
        fifteen._grid[2][3] = 11
        fifteen._grid[0][0] = 12
        # # print(fifteen)
        fifteen.solve_col0_tile(3)
        # # print(fifteen)
        # # print('========END SOLVE TILE IN COLUMN 0=========\n')
        # # # print('========LUCKY CASE WITH "UR"=========')
        fifteen = Puzzle(4, 4)
        fifteen._grid[3][0] = 0
        fifteen._grid[2][0] = 12
        fifteen._grid[0][0] = 8
        # # # print(fifteen)
        self.assertEqual(fifteen.solve_col0_tile(3), 'urrr', 'Test solve col0')
        self.assertEqual(fifteen._grid[2][3], 0, 'should be at end of row-1')
        # # # print(fifteen)
        # # # print('========END LUCKY CASE WITH "UR"========\n')
        # obj = Puzzle(3, 3, [[3, 2, 1], [6, 5, 4], [0, 7, 8]])
        # # print(obj)
        # self.assertEqual(obj.solve_col0_tile(2), 'urr')
        # # print(obj)
        # print()
        # print("================== I AM HERE==================")
        obj = Puzzle(4, 5, [[12, 11, 10, 9, 15],
                            [7, 6, 5, 4, 3],
                            [2, 1, 8, 13, 14],
                            [0, 16, 17, 18, 19]])
        # print(obj)
        self.assertEqual(obj.solve_col0_tile(3), 'uruurrrdllurdllurdlulddruldruldrdlurdluurddlurrrr')
        # print(obj)

    def test_solve_interior_tile_thirteen(self):
        fifteen = Puzzle(4, 4)
        # fifteen._grid[0][0] = 4
        # fifteen._grid[0][1] = 13
        # fifteen._grid[0][2] = 1
        # fifteen._grid[0][3] = 3
        # fifteen._grid[1][0] = 5
        # fifteen._grid[1][1] = 10
        # fifteen._grid[1][2] = 2
        # fifteen._grid[1][3] = 7
        # fifteen._grid[2][0] = 8
        # fifteen._grid[2][1] = 12
        # fifteen._grid[2][2] = 6
        # fifteen._grid[2][3] = 11
        # fifteen._grid[3][0] = 9
        # fifteen._grid[3][1] = 0
        # fifteen._grid[3][2] = 14
        # fifteen._grid[3][3] = 15
        fifteen.update_puzzle('dddruldrulurdruulddd')
        # # print('before solution call:\n', fifteen)
        zero_row, zero_col = fifteen.current_position(0, 0)
        # # print(fifteen.current_position(zero_row, zero_col))
        fifteen.update_puzzle('uuu')
        # # print('mid solution call:\n', fifteen)
        fifteen.update_puzzle('lddru')
        # # print('still mid solution call:\n', fifteen)
        fifteen.update_puzzle('lddruld')
        # uuu lddru lddru ld
        # # print('final solution call:\n', fifteen)
        self.assertEqual(fifteen.lower_row_invariant(3, 0), True)

    def test_row0_invariant(self):
        fifteen = Puzzle(4, 4, [[4, 2, 0, 3],
                                [5, 1, 6, 7],
                                [8, 9, 10, 11],
                                [12, 13, 14, 15]]
                         )
        # print('breh:\n', fifteen)
        self.assertEqual(fifteen.row0_invariant(2), True)

    def test_row1_invariant(self):
        fifteen = Puzzle(4, 4, [[4, 6, 1, 3],
                                [5, 2, 0, 7],
                                [8, 9, 10, 11],
                                [12, 13, 14, 15]]
                         )
        # # print('here:\n', fifteen)
        self.assertEqual(fifteen.row1_invariant(2), True)

        fifteen1 = Puzzle(4, 4, [[4, 6, 1, 3],
                                 [0, 2, 5, 7],
                                 [8, 9, 10, 11],
                                 [12, 13, 14, 15]]
                          )
        # # print('here:\n', fifteen)
        self.assertEqual(fifteen1.row1_invariant(2), False)

    def test_two_by_two(self):
        fifteen = Puzzle(2, 2)
        # # print('2x2:\n', fifteen)

    def test_three_by_two(self):
        fifteen = Puzzle(3, 2)
        fifteen._grid[0][0] = 2
        fifteen._grid[0][1] = 4
        fifteen._grid[1][0] = 3
        fifteen._grid[1][1] = 1
        fifteen._grid[2][0] = 0
        fifteen._grid[2][1] = 5
        # # print('3x2:\n', fifteen)
        fifteen.update_puzzle('uruld')
        # # print('3x2:\n', fifteen)
        fifteen.update_puzzle('ruldrdlurdluurddlur')  # solution to move BL tile
        # # print('3x2:\n', fifteen)

    def test_two_by_three(self):
        fifteen = Puzzle(2, 3)
        fifteen._grid[0][0] = 3
        fifteen._grid[0][1] = 1
        fifteen._grid[0][2] = 0
        fifteen._grid[1][0] = 2
        fifteen._grid[1][1] = 4
        fifteen._grid[1][2] = 5
        # # print(fifteen._grid[0].index(3))
        # # print('2x3:\n', fifteen)
        fifteen.update_puzzle('ldl')
        # # print('ldl:\n', fifteen)
        fifteen.update_puzzle('urdlurrdluldrruld')
        # # print('urdlurrdluldrruld:\n', fifteen)


if __name__ == '__main__':
    unittest.main()
