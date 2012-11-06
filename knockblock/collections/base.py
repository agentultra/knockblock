class Collection(object):

    def __init__(self, kblock, name, columns, keys=None):
        self._kblock = kblock

        self.name = name
        self.columns = tuple(columns)
        self.key_columns = tuple(keys) if keys else self.columns

        self._storage = []

    def insert(self, tup):
        self._storage.append(tup)

    def values(self):
        return self._storage
