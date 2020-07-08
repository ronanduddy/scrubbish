import unittest
from unittest.mock import patch
from scrubbish.request import Request


class TestRequest(unittest.TestCase):
    @patch("scrubbish.request.requests")
    def test_get(self, requests):
        requests.get.return_value = 200

        self.assertTrue(Request("example.com").get(0.001), 200)


if __name__ == "__main__":
    unittest.main()
