import unittest

from query.const import *

class TestConsts(unittest.TestCase):

    def test_select_all_exists(self):
        self.assertIsNotNone(SELECT_ALL, 'SELECT_ALL variable is None')

    def test_select_all_match_all_exists(self):
        self.assertIsNotNone(SELECT_ALL['match_all'], 'SELECT_ALL key [match_all] not found')

    def test_prefix_builder_method(self):
        self.assertEqual(prefix_builder('topics', 'wine'), {"bool": {"should": {"prefix": {"topics": "wine"}}}}, 'prefix_builder return wrong query')

    def test_wildcard_builder_method(self):
        self.assertEqual(wildcard_builder('name', 'cli'), {"wildcard": {"name": {"value": "*cli*"}}}, 'wildcard_builder return wrong query')
        
if __name__ == '__main__':
    unittest.main()