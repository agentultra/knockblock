import ast
import inspect
import re

from abc import ABCMeta, abstractmethod

from knockblock.exc import ProgrammingError


class KnockblockMeta(ABCMeta):

    def __init__(cls, name, bases, dct):
        return super(KnockblockMeta, cls).__init__(name, bases, dct)


class Knockblock(object):

    __metaclass__ = KnockblockMeta

    @abstractmethod
    def rules(self):
        pass
