import unittest as ut
from game import Game


class BowlingGameTest(ut.TestCase):
    def setUp(self):
        self.g = Game()

    def _roll_many(self, rolls, pins):
        for i in range(rolls):
            self.g.roll(pins)

    def test_gutter_game(self):
        self._roll_many(rolls=20, pins=0)
        self.assertEqual(0, self.g.score())

    def test_all_ones(self):
        self._roll_many(rolls=20, pins=1)
        self.assertEqual(20, self.g.score())

    def test_one_spare(self):
        self._roll_spare()
        self.g.roll(3)
        self._roll_many(17, 0)
        self.assertEqual(16, self.g.score())

    def test_one_strike(self):
        self._roll_strike()
        self.g.roll(3)
        self.g.roll(4)
        self._roll_many(16, 0)
        self.assertEqual(24, self.g.score())

    def test_perfect_game(self):
        self._roll_many(rolls=12, pins=10)
        self.assertEqual(300, self.g.score())

    def _roll_spare(self):
        self.g.roll(5)
        self.g.roll(5)

    def _roll_strike(self):
        self.g.roll(10)
