from abc import ABCMeta, abstractmethod


def monotone(funcobj):
    """
    A decorator indicating a monotone function.

    Requires that the class is derived from Lattice.  Is used by the
    Knockblock checker during CALM analysis.
    """
    funcobj.__ismonotonemethod__ = True
    return funcobj


def morphism(funcobj):
    """
    A decorator indicating a morphism function.

    Requires that the class is derived from Lattice.
    """
    funcobj.__ismorphismmethod__ = True
    return funcobj


class LatticeMeta(ABCMeta):
    def __new__(mcls, name, bases, namespace):
        cls = super(LatticeMeta, mcls).__new__(mcls, name, bases, namespace)
        monotones = set(name for name, value in namespace.items()
                        if getattr(value, "__ismonotonemethod__", False))
        morphisms = set(name for name, value in namespace.items()
                        if getattr(value, "__ismorphismmethod__", False))
        for base in bases:
            for name in getattr(base, "__monotonemethods__", set()):
                value = getattr(cls, name, None)
                if getattr(value, "__ismonotonemethod__", False):
                    monotones.add(name)
            for name in getattr(base, "__morphismmethods__", set()):
                value = getattr(cls, name, None)
                if getattr(value, "__ismorphismmethod__", False):
                    morphisms.add(name)
        cls.__monotonemethods__ = frozenset(monotones)
        cls.__morphismmethods__ = frozenset(morphisms)
        return cls


class Lattice(object):
    __metaclass__ = LatticeMeta

    @property
    def value(self):
        """
        Return the internal value of the Lattice.

        Note that this function is non-monotonic and should be called
        only by framework code.  Use with caution.
        """
        return self._value

    @abstractmethod
    def merge(self, other):
        pass

    def __eq__(self, other):
        if isinstance(other, Lattice):
            return self.value == other.value
        else:
            raise ValueError("You can only compare with another Lattice")
