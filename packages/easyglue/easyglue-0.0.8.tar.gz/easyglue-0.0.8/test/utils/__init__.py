import unittest


class TestUtils(unittest.TestCase):

    def test_validate_qualified_name(self):
        from easyglue.utils import validate_qualified_name
        database, table = validate_qualified_name("default.legislators")
        self.assertEqual("default", database)
        self.assertEqual("legislators", table)

    def test_validate_qualified_name_error(self):
        from easyglue.utils import validate_qualified_name
        self.assertRaises(ValueError, validate_qualified_name, "legislators")


if __name__ == '__main__':
    unittest.main()
