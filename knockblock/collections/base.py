class Collection(object):

    def __init__(self, kblock, name, schema):
        self._kblock = kblock

        self.name = name
        self.schema = schema

        self._storage = []

    def insert(self, tup):
        self._storage.append(tup)

    def values(self):
        return self._storage
