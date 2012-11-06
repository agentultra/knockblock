import mock
import unittest


from knockblock.collections.base import Collection


class TestCollection(unittest.TestCase):

    def test_insert(self):
        mock_block = mock.Mock()
        c = Collection(mock_block, "crew", ["name", "rank"])
        c.insert(("Jean-Luc Picard", "Captain"))
        self.assertEqual(c.values(), [("Jean-Luc Picard", "Captain")])
