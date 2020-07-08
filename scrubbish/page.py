import config
from bs4 import BeautifulSoup
from .request import Request

class Page:
    def __init__(self, uri):
        self.domain = config.DOMAIN
        self.uri = uri
        self.request = Request(self.url())
        self.soup = None

    def content(self):
        if self.soup is None:
            response = self.request.get()
            self.soup = BeautifulSoup(response.content, 'html.parser')

        return self.soup

    def next(self, uri):
        self.uri = uri
        self.soup = None

    def url(self):
        return '{domain}{uri}'.format(domain=self.domain, uri=self.uri)
