import unittest

from knockblock.lattices import (BoolLattice,
                                 DictLattice,
                                 MaxLattice,
                                 MinLattice,
                                 SetLattice)


class TestBoolLattice(unittest.TestCase):

    def test_merge(self):
        a = BoolLattice(False)
        b = BoolLattice(True)
        c = a.merge(b)
        self.assertTrue(c.value)


class TestDictLattice(unittest.TestCase):

    def test_initialize_without_lattice_value(self):
        bad = {"foo": 1}
        self.assertRaises(ValueError, DictLattice, bad)

    def test_merge(self):
        a = DictLattice({"foo": MaxLattice(1)})
        b = DictLattice({"bar": MaxLattice(2)})
        c = a.merge(b)
        self.assertEqual(c, DictLattice({"foo": MaxLattice(1),
                                         "bar": MaxLattice(2)}))

    def test_get_keys(self):
        a = DictLattice({"foo": MaxLattice(1)})
        self.assertEqual(a.keys(), SetLattice(["foo"]))

    def test_has_key(self):
        a = DictLattice({"foo": MaxLattice(1)})
        self.assertEqual(a.has_key("foo"), BoolLattice(True))

    def test_size(self):
        a = DictLattice({"foo": MaxLattice(1)})
        self.assertEqual(a.size, MaxLattice(1))


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


class TestMinLattice(unittest.TestCase):

    def test_merge(self):
        a = MinLattice(3)
        b = MinLattice(2)
        c = a.merge(b)
        self.assertEqual(c, MinLattice(2))

    def test_lt(self):
        a = MinLattice(3)
        b = MinLattice(2)
        c = b < a
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

    def test_contains(self):
        a = SetLattice([1, 2, 3])
        b = a.contains(2)
        c = a.contains(4)
        self.assertEqual(b, BoolLattice(True))
        self.assertEqual(c, BoolLattice(False))

    def test_size(self):
        a = SetLattice([1, 2, 3])
        self.assertEqual(a.size, MaxLattice(3))
