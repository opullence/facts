import unittest

from opulence.facts.person import Person


class TestPerson(unittest.TestCase):
    def test_simple_valid_person(self):
        john = Person(firstname="John", lastname="Snow")
        self.assertTrue(john.is_valid())

        fields = john.get_fields()
        self.assertEqual(john.plugin_category, "BaseFact")
        self.assertTrue("firstname" in fields)
        self.assertTrue("lastname" in fields)

    def test_invalid_person(self):
        john = Person()
        self.assertFalse(john.is_valid())

        fields = john.get_fields()
        self.assertEqual(john.plugin_category, "BaseFact")
        self.assertTrue("firstname" in fields)
        self.assertTrue("lastname" in fields)

    def test_invalid_person_bis(self):
        john = Person(firstname="John")
        self.assertFalse(john.is_valid())

        self.assertEqual(john.plugin_category, "BaseFact")
        fields = john.get_fields()
        self.assertTrue("firstname" in fields)
        self.assertTrue("lastname" in fields)