import mock
import operator
import unittest

from knockblock import exceptions as exc
from knockblock.collections.base import Collection


class TestCollection(unittest.TestCase):

    def setUp(self):
        self.mock_block = mock.Mock()

    def test_schema(self):
        c = Collection(self.mock_block, "crew",
                       ["name", "rank", "salary"],
                       keys=["name", "rank"])
        value_columns, key_columns = c.schema
        self.assertEqual(value_columns, ("salary",))
        self.assertEqual(key_columns, ("name", "rank"))

    def test_insert_a_tuple(self):
        c = Collection(self.mock_block, "crew", ["name", "rank"])
        c.insert(("Jean-Luc Picard", "Captain"))
        self.assertEqual(c._storage.values(),
                         [("Jean-Luc Picard", "Captain")])

    def test_insert_updated_value_raises_error(self):
        c = Collection(self.mock_block, "crew",
                       ["name", "rank", "salary"],
                       keys=["name", "rank"])
        c.insert(("Jean-Luc Picard", "Captain", 400))
        try:
            c.insert(("Jean-Luc Picard", "Captain", 100))
        except exc.KeyConstraintError:
            return True
        else:
            return False

    def test_get_a_tuple(self):
        c = Collection(self.mock_block, "crew",
                       ["name", "rank", "salary"],
                       keys=["name", "rank"])
        c.insert(("Jean-Luc Picard", "Captain", 400))
        c.insert(("Jeordi LaForge", "Engineer", 50))
        the_captain = c[("Jean-Luc Picard", "Captain")]
        self.assertEqual(the_captain.name, "Jean-Luc Picard")
        self.assertEqual(the_captain.rank, "Captain")
        self.assertEqual(the_captain.salary, 400)

    def test_projection(self):
        c = Collection(self.mock_block, "crew",
                       ["name", "rank", "salary"],
                       keys=["name", "rank"])
        c.insert(("Jean-Luc Picard", "Captain", 400))
        c.insert(("Jeordi LaForge", "Engineer", 50))
        tups = c._project(lambda t: [t.name, t.salary])
        self.assertEqual(len(tups), 2)
        self.assertEqual(len(tups[0]), 2)
        names = map(lambda t: t[0], tups)
        self.assertTrue("Jean-Luc Picard" in names)
        self.assertTrue("Jeordi LaForge" in names)

    def test_get_keys(self):
        c = Collection(self.mock_block, "crew",
                       ["name", "rank", "salary"],
                       keys=["name", "rank"])
        c.insert(("Jean-Luc Picard", "Captain", 400))
        c.insert(("Jeordi LaForge", "Engineer", 50))
        keys = c.keys()
        self.assertTrue(len(keys), 2)
        self.assertTrue(len(keys[0]), 2)
        names = map(lambda k: k[0], keys)
        ranks = map(lambda k: k[1], keys)
        self.assertTrue("Jean-Luc Picard" in names)
        self.assertTrue("Jeordi LaForge" in names)
        self.assertTrue("Captain" in ranks)
        self.assertTrue("Engineer" in ranks)

    def test_get_values(self):
        c = Collection(self.mock_block, "crew",
                       ["name", "rank", "salary"],
                       keys=["name", "rank"])
        c.insert(("Jean-Luc Picard", "Captain", 400))
        c.insert(("Jeordi LaForge", "Engineer", 50))
        vals = c.values()
        self.assertEqual(len(vals), 2)
        self.assertEqual(len(vals[0]), 1)
        salaries = map(lambda t: t[0], vals)
        self.assertTrue(400 in salaries)
        self.assertTrue(50 in salaries)

    def test_has_key(self):
        c = Collection(self.mock_block, "crew",
                       ["name", "rank", "salary"],
                       keys=["name", "rank"])
        c.insert(("Jean-Luc Picard", "Captain", 400))
        c.insert(("Jeordi LaForge", "Engineer", 50))
        self.assertTrue(("Jean-Luc Picard", "Captain") in c)

    def test_does_not_have_key(self):
        c = Collection(self.mock_block, "crew",
                       ["name", "rank", "salary"],
                       keys=["name", "rank"])
        c.insert(("Jean-Luc Picard", "Captain", 400))
        c.insert(("Jeordi LaForge", "Engineer", 50))
        self.assertFalse(("James Kirk", "Captain") in c)

    def test_sort_collection(self):
        c = Collection(self.mock_block, "crew",
                       ["name", "rank", "salary"],
                       keys=["name", "rank"])
        c.insert(("Jean-Luc Picard", "Captain", 400))
        c.insert(("Jeordi LaForge", "Engineer", 50))
        sorted_values = c.sort(key=operator.attrgetter("salary"))
        self.assertEqual(sorted_values,
                         [("Jeordi LaForge", "Engineer", 50),
                          ("Jean-Luc Picard", "Captain", 400)])

    def test_merge(self):
        c = Collection(self.mock_block, "crew",
                       ["name", "rank", "salary"],
                       keys=["name", "rank"])
        c.merge([("Jeordi LaForge", "Engineer", 50),
                 ("Jean-Luc Picard", "Captain", 400)])
        names = [t.name for t in c._storage.values()]
        self.assertTrue("Jean-Luc Picard" in names)
        self.assertTrue("Jeordi LaForge" in names)

    def test_len(self):
        c = Collection(self.mock_block, "crew",
                       ["name", "rank", "salary"],
                       keys=["name", "rank"])
        c.merge([("Jeordi LaForge", "Engineer", 50),
                 ("Jean-Luc Picard", "Captain", 400)])
        self.assertEqual(len(c), 2)

    def test_tick_raises_NotImplemented(self):
        c = Collection(self.mock_block, "crew",
                       ["name", "rank", "salary"],
                       keys=["name", "rank"])
        self.assertRaises(NotImplementedError,
                          c.tick)
