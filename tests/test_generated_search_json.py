# approval test to verify that the search.json file is generated correctly
import unittest
from pathlib import Path
from approvaltests import verify

# go in to _site and read search.json and approve it
class Test(unittest.TestCase):
    def test_search_json(self):
        path = Path('_site/search.json')
        verify(path.read_text())