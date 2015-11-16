import unittest
from fifteen import Puzzle


class TestFifteen(unittest.TestCase):
    def test_lower_row_invariant(self):
        fifteen = Puzzle(4, 4)
        fifteen._grid[0][0], fifteen._grid[2][1] = fifteen._grid[2][1], \
                                                   fifteen._grid[0][0]
        self.assertEqual(fifteen.lower_row_invariant(2, 1), True)

        fifteen = Puzzle(4, 4)
        fifteen._grid[0][0], fifteen._grid[2][1] = fifteen._grid[2][1], \
                                                   fifteen._grid[0][0]
        fifteen._grid[0][1], fifteen._grid[3][2] = fifteen._grid[3][2], \
                                                   fifteen._grid[0][1]
        self.assertEqual(fifteen.lower_row_invariant(2, 1), False)

        fifteen = Puzzle(4, 4)
        self.assertEqual(fifteen.lower_row_invariant(0, 0), True)

        fifteen = Puzzle(4, 4)
        fifteen._grid[0][1], fifteen._grid[0][2] = fifteen._grid[0][2], \
                                                   fifteen._grid[0][1]
        self.assertEqual(fifteen.lower_row_invariant(0, 0), False)

    def test_solve_interior_tile(self):
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

        fifteen.solve_interior_tile(3, 1)

        self.assertEqual(fifteen.lower_row_invariant(3, 0), True)

        fifteen = Puzzle(4, 4)
        fifteen._grid[0][0] = 14
        fifteen._grid[3][2] = 0

        fifteen.solve_interior_tile(3, 2)

        solved_through_strings = Puzzle(4, 4)
        solved_through_strings._grid[0][0] = 14
        solved_through_strings._grid[3][2] = 0
        solved_through_strings.update_puzzle('uuulldrruldrulddrulddruld')
        for val1, val2 in zip(fifteen._grid, solved_through_strings._grid):
            assert val1 == val2

        fifteen = Puzzle(4, 4)
        fifteen._grid[0][0] = 3
        fifteen._grid[0][-1] = 13
        fifteen._grid[3][1] = 0

        fifteen.solve_interior_tile(3, 1)

        fifteen = Puzzle(4, 4)
        fifteen._grid[2][1] = 10
        fifteen._grid[2][2] = 0
        fifteen._grid[0][0] = 9

        fifteen.solve_interior_tile(2, 2)

        fifteen = Puzzle(4, 4)
        fifteen._grid[2][1] = 11
        fifteen._grid[2][-1] = 0
        fifteen._grid[0][0] = 9

        fifteen.solve_interior_tile(2, 3)

    def test_helper_solve_interior(self):
        fifteen = Puzzle(4, 4, [[4, 13, 1, 3],
                                [5, 10, 2, 7],
                                [8, 12, 6, 11],
                                [9, 0, 14, 15]]
                         )

        computed = fifteen.helper_solve_interior(target_solved_row=2, target_solved_col=2,
                                                 zero_row=3, zero_col=1,
                                                 solved_val_row=0, solved_val_col=1)
        self.assertEqual(computed, 'uulddruld')

        fifteen = Puzzle(4, 4, [[4, 13, 1, 3],
                                [5, 10, 2, 7],
                                [8, 12, 6, 11],
                                [9, 0, 14, 15]]
                         )

        computed = fifteen.helper_solve_interior(0, 3, zero_row=3, zero_col=1,
                                                 solved_val_row=0, solved_val_col=1)

    def test_solve_col0_tile(self):
        fifteen = Puzzle(4, 4)
        fifteen._grid[3][0] = 0
        fifteen._grid[2][3] = 11
        fifteen._grid[0][0] = 12

        fifteen.solve_col0_tile(3)

        fifteen = Puzzle(4, 4)
        fifteen._grid[3][0] = 0
        fifteen._grid[2][0] = 12
        fifteen._grid[0][0] = 8

        self.assertEqual(fifteen.solve_col0_tile(3), 'urrr', 'Test solve col0')
        self.assertEqual(fifteen._grid[2][3], 0, 'should be at end of row-1')

        obj = Puzzle(4, 5, [[12, 11, 10, 9, 15],
                            [7, 6, 5, 4, 3],
                            [2, 1, 8, 13, 14],
                            [0, 16, 17, 18, 19]])

        self.assertEqual(obj.solve_col0_tile(3), 'uruurrrdllurdllurdlulddruldruldrdlurdluurddlurrrr')

    def test_row0_invariant(self):
        fifteen = Puzzle(4, 4, [[4, 2, 0, 3],
                                [5, 1, 6, 7],
                                [8, 9, 10, 11],
                                [12, 13, 14, 15]]
                         )

    def test_row1_invariant(self):
        fifteen = Puzzle(4, 4, [[4, 6, 1, 3],
                                [5, 2, 0, 7],
                                [8, 9, 10, 11],
                                [12, 13, 14, 15]]
                         )

        self.assertEqual(fifteen.row1_invariant(2), True)

        fifteen1 = Puzzle(4, 4, [[4, 6, 1, 3],
                                 [0, 2, 5, 7],
                                 [8, 9, 10, 11],
                                 [12, 13, 14, 15]]
                          )

        self.assertEqual(fifteen1.row1_invariant(2), False)

    def test_solve_row0_tile(self):
        fifteen = Puzzle(4, 4, [[4, 5, 0, 3],
                                [2, 1, 6, 7],
                                [8, 9, 10, 11],
                                [12, 13, 14, 15]]
                         )
        self.assertEqual(fifteen.solve_row0_tile(2), 'ldlurdlurrdluldrruld')

        fifteen = Puzzle(4, 5, [[1, 2, 0, 3, 4],
                                [6, 5, 7, 8, 9],
                                [10, 11, 12, 13, 14],
                                [15, 16, 17, 18, 19]])
        self.assertEqual(fifteen.solve_row0_tile(2), 'ld')

    def test_solve_row1_tile(self):
        fifteen = Puzzle(4, 4, [[4, 6, 1, 3],
                                [5, 2, 0, 7],
                                [8, 9, 10, 11],
                                [12, 13, 14, 15]]
                         )
        self.assertEqual(fifteen.solve_row1_tile(2), 'uldruldur')
        fifteen = Puzzle(4, 5, [[7, 6, 5, 3, 4],
                                [2, 1, 0, 8, 9],
                                [10, 11, 12, 13, 14],
                                [15, 16, 17, 18, 19]])
        self.assertEqual(fifteen.solve_row1_tile(2), 'ulldrruldruldur')

    def test_solve_2x2(self):
        fifteen = Puzzle(2, 2, [[3, 2],
                                [1, 0]]
                         )
        fifteen.solve_2x2()
        solved_fifteen = Puzzle(2, 2, [[0, 1],
                                       [2, 3]]
                                )
        self.assertEqual(fifteen._grid, solved_fifteen._grid)

        fifteen = Puzzle(3, 3, [[4, 3, 2],
                                [1, 0, 5],
                                [6, 7, 8]]
                         )
        solved_fifteen = Puzzle(3, 3, [[0, 1, 2],
                                       [3, 4, 5],
                                       [6, 7, 8]]
                                )
        fifteen.solve_2x2()
        self.assertEqual(fifteen._grid, solved_fifteen._grid)

        fifteen = Puzzle(5, 4, [[5, 4, 2, 3],
                                [1, 0, 6, 7],
                                [8, 9, 10, 11],
                                [12, 13, 14, 15],
                                [16, 17, 18, 19]])
        solved_fifteen = Puzzle(5, 4, [[0, 1, 2, 3],
                                       [4, 5, 6, 7],
                                       [8, 9, 10, 11],
                                       [12, 13, 14, 15],
                                       [16, 17, 18, 19]])
        fifteen.solve_2x2()
        self.assertEqual(fifteen._grid, solved_fifteen._grid)

    def test_solve_puzzle(self):
        fifteen = Puzzle(4, 4, [[5, 3, 6, 7],
                                [2, 14, 15, 9],
                                [11, 8, 4, 1],
                                [0, 10, 13, 12]]

                         )
        # print(fifteen)
        # fifteen.solve_puzzle()
        # print(fifteen)

        fifteen = Puzzle(3, 3, [[8, 7, 6],
                                [5, 4, 3],
                                [2, 1, 0]]
                         )
        # print(fifteen)
        # fifteen.solve_puzzle()
        # print(fifteen)

        fifteen = Puzzle(4, 5, [[15, 16, 0, 3, 4],
                                [5, 6, 7, 8, 9],
                                [10, 11, 12, 13, 14],
                                [1, 2, 17, 18, 19]]
                         )
        # print(fifteen)
        # fifteen.solve_puzzle()
        # print(fifteen)
        fifteen = Puzzle(4, 5, [[15, 16, 0, 3, 4],
                                [5, 6, 7, 8, 9],
                                [10, 11, 12, 13, 14],
                                [1, 2, 17, 18, 19]],
                         'UNDER CONSTRUCTION'
                         )
        # print(fifteen)
        # print(fifteen.solve_puzzle())
        # print(fifteen)

        fifteen = Puzzle(2, 4, [[0, 3, 2, 7],
                                [4, 5, 6, 1]],
                         'UNDER CONSTRUCTION'
                         )
        print(fifteen)
        fifteen.solve_puzzle()


if __name__ == '__main__':
    unittest.main()
