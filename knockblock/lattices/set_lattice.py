from . bool_lattice import BoolLattice
from . max_lattice import MaxLattice
from knockblock.lattices.base import Lattice, monotone, morphism


class SetLattice(Lattice):

    def __init__(self, elements):
        self._value = set(elements)

    def merge(self, other):
        if isinstance(other, SetLattice):
            return SetLattice(self._value | other.value)
        else:
            raise ValueError("You can only merge another SetLattice")

    @monotone
    def intersect(self, other):
        return SetLattice(self._value & other.value)

    @morphism
    def contains(self, item):
        return BoolLattice(item in self._value)

    @property
    @monotone
    def size(self):
        return MaxLattice(len(self._value))
