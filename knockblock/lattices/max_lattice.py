from . bool_lattice import BoolLattice
from knockblock.lattices.base import Lattice, morphism


class MaxLattice(Lattice):

    def __init__(self, x):
        self._value = x

    def merge(self, other):
        val = other.value if other.value > self.value else self.value
        return MaxLattice(val)

    @morphism
    def __gt__(self, other):
        return BoolLattice(other.value < self.value)

    @morphism
    def __ge__(self, other):
        return BoolLattice(other.value <= self.value)
