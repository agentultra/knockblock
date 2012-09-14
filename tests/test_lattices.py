import unittest

from knockblock.lattices import SetLattice


class TestSetLattice(unittest.TestCase):

    def test_merge(self):
        a = SetLattice([1, 2])
        b = SetLattice([3, 4])
        a.merge(b)
        self.assertEqual(a, SetLattice([1, 2, 3, 4]))
