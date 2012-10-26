import unittest

#from knockblock import Knockblock
from knockblock.meta import Knockblock
from knockblock.exc import ProgrammingError


class TestMeta(unittest.TestCase):

    def test_missing_rules(self):
        raise unittest.SkipTest

        class TestReplica(object):
            __metaclass__ = Knockblock

            def rules(self):
                pass

        self.assertRaises(ProgrammingError,
                          TestReplica)
