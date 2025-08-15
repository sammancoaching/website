# approval test to verify that the search.json file is generated correctly
import unittest
from pathlib import Path
import json
from approvaltests import verify_as_json

# go in to _site and read search.json and approve it
class Test(unittest.TestCase):
    def test_search_json(self):
        path = Path('_site/search.json')
        data = json.loads(path.read_text(encoding='utf-8'))
        verify_as_json(data)