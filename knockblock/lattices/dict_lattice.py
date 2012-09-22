from collections import Mapping
from copy import deepcopy

from . bool_lattice import BoolLattice
from . max_lattice import MaxLattice
from . set_lattice import SetLattice
from knockblock.lattices.base import Lattice, monotone, morphism


class DictLattice(Lattice):

    def __init__(self, val):
        if isinstance(val, Mapping):
            for v in val.values():
                if not isinstance(v, Lattice):
                    raise ValueError("Dict values must be lattices")
            self._value = val
        else:
            raise ValueError("DictLattice can only be initialized with "
                             "a valid Mapping value.")

    def merge(self, other):
        val = deepcopy(self._value)
        for k, v in other.items():
            if k in val:
                val[k].merge(v)
            else:
                val[k] = v
        return DictLattice(val)

    @property
    @morphism
    def size(self):
        return MaxLattice(len(self._value))

    @morphism
    def keys(self):
        return SetLattice(self._value.keys())

    @morphism
    def has_key(self, key):
        return BoolLattice(key in self._value)
