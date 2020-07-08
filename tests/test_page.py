import unittest
from unittest.mock import Mock
from unittest.mock import patch
from props.page import Page

class TestPage(unittest.TestCase):
    @patch('props.page.Request', autospec=True)
    def setUp(self, request):
        self.request = request
        self.request.return_value.get.return_value = Mock(content='<html>hello</html>')
        
        self.page = Page('/location')
        self.page.domain = 'example.com'

    def test_content(self):
        self.assertEqual(self.page.content().text, 'hello')

    def test_next(self):
        self.assertEqual(self.page.uri, '/location')

        self.page.next('/next-location')
        self.assertEqual(self.page.uri, '/next-location')

    def test_url(self):
        self.assertEqual(self.page.url(), 'example.com/location')

if __name__ == '__main__':
    unittest.main()
