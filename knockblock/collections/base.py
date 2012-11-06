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
        fact = self._struct(*tup)
        key = tuple([attrgetter(k)(fact) for k in self.key_columns])
        self._storage[key] = fact

    def values(self):
        return self._storage.values()

    def __getitem__(self, key):
        return self._storage.get(key)
