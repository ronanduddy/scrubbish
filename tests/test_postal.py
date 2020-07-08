import unittest
from scrubbish.postal import Postal


class TestPostal(unittest.TestCase):
    def test_info_not_found(self):
        address = "1 street, Belfast BT123 123"

        result = Postal(address).info()
        expected = {
            "coverage": "?",
            "district": "bt123",
            "position": "?",
            "post_town": "?",
        }
        self.assertEqual(result, expected)

    def test_info(self):
        address = "1 street, Belfast BT9 123"

        result = Postal(address).info()
        expected = {
            "coverage": "Belfast, Malone, Lisburn Road, Taughmonagh, Stranmillis",
            "district": "bt9",
            "position": "south",
            "post_town": "Belfast",
        }

        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
