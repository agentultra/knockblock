import unittest

from knockblock.lattices import SetLattice


class TestSetLattice(unittest.TestCase):

    def test_merge(self):
        a = SetLattice([1, 2])
        b = SetLattice([3, 4])
        self.assertEqual(a.merge(b), SetLattice([1, 2, 3, 4]))

    def test_intersect(self):
        a = SetLattice([1, 2])
        b = SetLattice([1, 3])
        self.assertEqual(a.intersect(b), SetLattice([1]))
