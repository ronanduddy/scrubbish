import unittest
from unittest.mock import Mock
from props.properties import Properties

class TestProperties(unittest.TestCase):
    def setUp(self):
        self.properties = Properties('over_there')

    def stub_request(self, content):
        attributes = {'get.return_value': Mock(content=content)}
        self.properties.request = Mock(**attributes)

    def test_more_when_divs(self):
        content =   """
                    <html>
                        <div class="propbox-details"></div>
                        <div class="propbox-details"></div>
                    </html>
                    """
        self.stub_request(content)

        self.assertTrue(self.properties.more())

    def test_more_when_no_divs(self):
        content =   """
                    <html>
                        <div class="propbox-details"></div>
                    </html>
                    """
        self.stub_request(content)

        self.assertFalse(self.properties.more())

    def test_more_when_next_button(self):
        content =   """
                    <html>
                        <a class="btn paging-next"></a>
                    </html>
                    """
        self.stub_request(content)

        self.assertTrue(self.properties.more())

    def test_more_when_no_next_button(self):
        content =   """
                    <html>
                        <a class=""></a>
                    </html>
                    """
        self.stub_request(content)

        self.assertFalse(self.properties.more())

    def test_next_uri(self):
        first_page =    """
                        <html>
                            <a href="hello1"><div class="propbox-details"></div></a>
                            <a href="hello2"><div class="propbox-details"></div></a>
                            <a href="/next_page" class="btn paging-next">next page</a>
                        </html>
                        """
        self.stub_request(first_page)

        self.assertEqual(self.properties.next_uri(), 'hello1')
        self.assertEqual(self.properties.next_uri(), 'hello2')

        second_page =   """
                        <html>
                            <a href="hello3"><div class="propbox-details"></div></a>
                            <a href="hello4"><div class="propbox-details"></div></a>
                        </html>
                        """
        self.stub_request(second_page)

        self.assertEqual(self.properties.next_uri(), 'hello3')
        self.assertEqual(self.properties.next_uri(), 'hello4')

    def test_pagination(self):
        content =   """
                    <span class="pgheader-currentpage">Page 1 of 1 (<em>1</em> things)</span>
                    """
        self.stub_request(content)

        self.assertEqual(self.properties.pagination(), 'Page 1 of 1 (1 things)')

if __name__ == '__main__':
    unittest.main()
