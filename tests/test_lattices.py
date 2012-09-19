import unittest

from knockblock.lattices import BoolLattice, MaxLattice, SetLattice


class TestBoolLattice(unittest.TestCase):

    def test_merge(self):
        a = BoolLattice(False)
        b = BoolLattice(True)
        c = a.merge(b)
        self.assertTrue(c.value)


class TestMaxLattice(unittest.TestCase):

    def test_merge(self):
        a = MaxLattice(2)
        b = MaxLattice(3)
        c = a.merge(b)
        self.assertEqual(c, MaxLattice(3))

    def test_gt(self):
        a = MaxLattice(2)
        b = MaxLattice(3)
        c = b > a
        self.assertEqual(c, BoolLattice(True))

    def test_gte(self):
        a = MaxLattice(2)
        b = MaxLattice(2)
        c = b >= a
        self.assertEqual(c, BoolLattice(True))


class TestSetLattice(unittest.TestCase):

    def test_merge(self):
        a = SetLattice([1, 2])
        b = SetLattice([3, 4])
        self.assertEqual(a.merge(b), SetLattice([1, 2, 3, 4]))

    def test_intersect(self):
        a = SetLattice([1, 2])
        b = SetLattice([1, 3])
        self.assertEqual(a.intersect(b), SetLattice([1]))
