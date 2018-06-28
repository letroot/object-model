import csv
import unittest

from rap_library import LIBRARY_CSV, Album, raplib


# we start by turning errors into failures
# and then onward!
class TestCase(unittest.TestCase):

    def setUp(self):
        with open(LIBRARY_CSV, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            self.records = [Album(rapper=row['rapper'],
                                 title=row['title'],
                                 year=row['year']) for row in reader]

    def test_album_not_none(self):
        self.assertIsNotNone(raplib.albums)

    def test_album_length(self):
        self.assertEqual(len(raplib.albums), len(self.records))

    def test_contains_album(self):
        self.assertTrue(self.records[0] in raplib)

    def test_library_length(self):
        self.assertEqual(len(raplib), len(self.records))

    def test_get_item(self):
        self.assertEqual(raplib[4], self.records[4])
        self.assertEqual(raplib[0], self.records[0])


if __name__ == '__main__':
    unittest.main()
