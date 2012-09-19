from . bool_lattice import BoolLattice
from knockblock.lattices.base import Lattice, morphism


class MinLattice(Lattice):

    def __init__(self, val):
        self._value = val

    def merge(self, other):
        val = other.value if other.value < self._value else self._value
        return MinLattice(val)

    @morphism
    def __lt__(self, other):
        return BoolLattice(other.value > self._value)
