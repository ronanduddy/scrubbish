import unittest
from unittest.mock import patch
from props.request import Request

class TestRequest(unittest.TestCase):
    @patch('props.request.requests')
    def test_get(self, requests):
        requests.get.return_value = 200

        self.assertTrue(Request('example.com').get(.001), 200)

if __name__ == '__main__':
    unittest.main()
