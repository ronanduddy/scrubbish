import unittest
import os
from props.json_helper import JsonHelper

class TestJsonHelper(unittest.TestCase):
    def setUp(self):
        filename = 'test'
        directory = 'tests/json'

        self.json_helper = JsonHelper(filename)
        self.json_helper.directory = directory

        if not os.path.exists(directory):
            os.makedirs(directory)

    def tearDown(self):
        directory = self.json_helper.directory
        files = [ file for file in os.listdir(directory) if file.endswith('.json') ]

        for file in files:
            os.remove(os.path.join(directory, file))

        os.rmdir(os.path.join(directory))

    def filename(self):
        """ Helper function however, duplication here and in CsvHelper. """
        directory = self.json_helper.directory
        name = self.json_helper.filename
        creation = self.json_helper.creation

        return f'{directory}/{name}_{creation}.json'

    def test_dump(self):
        self.json_helper.dump({'foo': 'bar'})

        json_file = open(self.filename(), 'r')
        self.assertEqual(json_file.read(), '{"foo": "bar"}')
        json_file.close()

    def test_read(self):
        self.json_helper.dump({'foo': 'bar'})
        name = self.filename()

        self.assertEqual(JsonHelper(name).read(), {'foo': 'bar'})

if __name__ == '__main__':
    unittest.main()
