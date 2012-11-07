from collections import namedtuple
from operator import attrgetter


class Collection(object):

    def __init__(self, kblock, name, columns, keys=None):
        self._kblock = kblock

        self.name = name
        self.columns = tuple(columns)
        self.key_columns = tuple(keys) if keys else self.columns

        self._struct = namedtuple(self.name, self.columns)
        self._storage = {}

    def insert(self, tup):
        """
        Insert a new fact into the collection.

        :param tup: An iterable object whose values should correspond
                    to the given schema of the collection.
        """
        fact = self._struct(*tup)
        key = tuple([attrgetter(k)(fact) for k in self.key_columns])
        self._storage[key] = fact

    def keys(self):
        """
        Return a list of tuples from the key values of the collection.

        It is important to note that this method is the keys
        relational operator and does not have the same meaning as the
        Python dictionary method.

        :returns: A list of tuples.
        """
        return self._storage.keys()

    def values(self):
        """
        Return a list of tuples from the non-key values of the
        collection.

        It is important to note that this method is the values
        relational operator and does not have the same meaning as the
        Python dictionary method.

        :returns: A list of tuples.
        """
        value_columns = [c for c in self.columns if
                         c not in self.key_columns]
        return self._project(lambda t: [attrgetter(k)(t) for
                                        k in value_columns])

    def _project(self, func):
        """
        Return a list of tuples.

        The function passed to _project receives a single fact from
        the collection and its return value is wrapped by tuple().

        :param func: A function taking a single fact as its parameter
                     and returning an iterable.
        :return: A list of tuples.
        """
        return [tuple(func(t)) for t in self._storage.values() if
                t is not None]

    def __getitem__(self, key):
        """
        Return a fact from the collection.

        :param key: A tuple of values that form the key of the fact.
        """
        return self._storage.get(key)

    def __contains__(self, key):
        return True if self._storage.get(key) else False
