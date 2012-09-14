from knockblock.lattices.base import Lattice


class SetLattice(Lattice):

    def __init__(self, elements):
        self._value = set(elements)

    def merge(self, other):
        if isinstance(other, SetLattice):
            self._value |= other.value
        else:
            raise ValueError("You can only merge another SetLattice")

    def __eq__(self, other):
        if isinstance(other, SetLattice):
            return self._value == other.value
        else:
            raise ValueError("You can only compare with another SetLattice")
