import mock
import unittest


from knockblock.collections.base import Collection


class TestCollection(unittest.TestCase):

    def setUp(self):
        self.mock_block = mock.Mock()

    def test_schema(self):
        c = Collection(self.mock_block, "crew",
                       ["name", "rank", "salary"],
                       keys=["name", "rank"])
        self.assertEqual(c.key_columns, ("name", "rank"))
        self.assertEqual(c.columns, ("name", "rank", "salary"))

    def test_insert_a_tuple(self):
        c = Collection(self.mock_block, "crew", ["name", "rank"])
        c.insert(("Jean-Luc Picard", "Captain"))
        self.assertEqual(c.values(), [("Jean-Luc Picard", "Captain")])

    def test_get_a_tuple(self):
        c = Collection(self.mock_block, "crew",
                       ["name", "rank", "salary"],
                       keys=["name", "rank"])
        c.insert(("Jean-Luc Picard", "Captain", 400))
        c.insert(("Jeordi LaForge", "Engineer", 50))
        self.assertEqual(c[("Jean-Luc Picard", "Captain")],
                         ("Jean-Luc Picard", "Captain", 400))
