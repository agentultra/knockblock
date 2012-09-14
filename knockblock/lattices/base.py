from abc import ABCMeta, abstractmethod


class Lattice(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def merge(self, other):
        pass

    @property
    def value(self):
        """
        Return the internal value of the Lattice.

        Note that this function is non-monotonic and should be called
        only by framework code.  Use with caution.
        """
        return self._value
