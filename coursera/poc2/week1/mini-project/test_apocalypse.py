from unittest import TestCase
from zombie_apocalypse_bfs import Apocalypse

__author__ = 'ChessTastic'


class TestApocalypse(TestCase):
  def test_num_humans(self):
    state = Apocalypse(5, 5)
    state.add_human(2, 3)
    self.assertEqual(state.num_humans(), 1, "test 1")
