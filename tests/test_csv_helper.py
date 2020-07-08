import unittest
import os
from scrubbish.csv_helper import CsvHelper


class TestCsvHelper(unittest.TestCase):
    def setUp(self):
        filename = "test"
        directory = "tests/csv"

        self.csv_helper = CsvHelper(filename)
        self.csv_helper.directory = directory

        if not os.path.exists(directory):
            os.makedirs(directory)

    def tearDown(self):
        directory = self.csv_helper.directory
        files = [file for file in os.listdir(directory) if file.endswith(".csv")]

        for file in files:
            os.remove(os.path.join(directory, file))

        os.rmdir(os.path.join(directory))

        self.csv_helper.file.close()

    def filename(self):
        """ Helper function however, duplication here and in CsvHelper. """
        directory = self.csv_helper.directory
        name = self.csv_helper.filename
        creation = self.csv_helper.creation

        return f"{directory}/{name}_{creation}.csv"

    def create_csv(self):
        """ Helper function to create test csv file. """
        row = {"header1": "foo", "header2": "bar"}
        self.csv_helper.write(row)
        self.csv_helper.file.close()

    def test_write(self):
        row = {"header1": "foo", "header2": "bar"}

        self.assertIsNone(self.csv_helper.file)
        self.assertIsNone(self.csv_helper.fieldnames)
        self.assertIsNone(self.csv_helper.writer)

        self.csv_helper.write(row)

        self.assertIsNotNone(self.csv_helper.file)
        self.assertIsNotNone(self.csv_helper.fieldnames)
        self.assertIsNotNone(self.csv_helper.writer)

        self.csv_helper.file.close()

        csv_file = open(self.filename(), "r")
        expected = "header1,header2\nfoo,bar\n"
        self.assertEqual(csv_file.read(), expected)
        csv_file.close()

    def test_append(self):
        self.create_csv()
        directory = self.csv_helper.directory

        self.csv_helper = CsvHelper(self.filename())
        self.csv_helper.directory = directory

        new_row = {"header1": "baz", "header2": "fizz"}

        self.assertIsNone(self.csv_helper.file)
        self.assertIsNone(self.csv_helper.fieldnames)
        self.assertIsNone(self.csv_helper.writer)

        self.csv_helper.append(new_row)

        self.assertIsNotNone(self.csv_helper.file)
        self.assertIsNotNone(self.csv_helper.fieldnames)
        self.assertIsNotNone(self.csv_helper.writer)

        self.csv_helper.file.close()

        csv_file = open(self.csv_helper.filename, "r")
        expected = "header1,header2\nfoo,bar\nbaz,fizz\n"
        self.assertEqual(csv_file.read(), expected)
        csv_file.close()

    def test_read(self):
        self.create_csv()
        directory = self.csv_helper.directory

        self.csv_helper = CsvHelper(self.filename())
        self.csv_helper.directory = directory

        expected = [{"header1": "foo", "header2": "bar"}]
        for index, row in enumerate(self.csv_helper.read()):
            self.assertEqual(row, expected[index])


if __name__ == "__main__":
    unittest.main()
