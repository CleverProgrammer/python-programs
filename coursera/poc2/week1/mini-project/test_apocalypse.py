import zombie_apocalypse_bfs
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
      self.assertEqual(state.num_humans(), 0, "test clear")

  def test_compute_distance_field(self):
      state = Apocalypse(5, 5)
      state.add_human(2, 3)
      state.add_human(1, 2)
      self.assertEqual(state.num_humans(), 2)
      state.add_zombie(4, 3)
      state.add_zombie(2, 2)
      self.assertEqual(state.num_zombies(), 2)
      human_field = state.compute_distance_field(zombie_apocalypse_bfs.HUMAN)
      print(human_field)
      print(state.boundary)
      print(state.visited)
      self.assertEqual(state.visited.is_empty(1,2), False, "test human_field")


