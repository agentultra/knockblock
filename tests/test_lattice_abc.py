import unittest

from knockblock.lattices.base import Lattice, monotone, morphism


class TestLatticeABC(unittest.TestCase):

    def test_monotone_methods(self):
        class MyLattice(Lattice):

            def merge(self):
                pass

            @monotone
            def my_monotonic_method(self, a):
                return a

        x = MyLattice()

        self.assertTrue("my_monotonic_method" in x.__monotonemethods__)
        self.assertEqual(len(x.__monotonemethods__), 1)

    def test_morphism_methods(self):
        class MyLattice(Lattice):

            def merge(self):
                pass

            @morphism
            def my_morphism_method(self, a):
                return a

        x = MyLattice()

        self.assertTrue("my_morphism_method" in x.__morphismmethods__)
        self.assertEqual(len(x.__morphismmethods__), 1)
