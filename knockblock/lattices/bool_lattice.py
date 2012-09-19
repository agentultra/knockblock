from knockblock.lattices.base import Lattice


class BoolLattice(Lattice):

    def __init__(self, val):
        if isinstance(val, bool):
            self._value = val
        else:
            raise ValueError("BoolLattice can only be instantiated with "
                             "a boolean value.")

    def merge(self, other):
        return BoolLattice(self.value or other.value)
