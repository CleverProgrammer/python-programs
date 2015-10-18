from unittest import TestCase
from zombie_apocalypse_bfs import Apocalypse

__author__ = 'ChessTastic'


class TestApocalypse(TestCase):
  """
  test cases for the zombie apocalypse class
  """

  def test_num_humans(self):
    state = Apocalypse(5, 5)
    state.add_human(2, 3)
    self.assertEqual(state.num_humans(), 1, "test num humans")

  def test_clear(self):
      state = Apocalypse(5, 5)
      state.add_human(2, 3)
      state.add_human(1, 2)
      self.assertEqual(state.num_humans(), 2)
      state.clear()
      self.assertEqual(state.num_humans(), 0)

  def test_compute_distance_field(self):
      state = Apocalypse(5, 5)


