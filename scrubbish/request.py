import requests
import time
import random


class Request:
    def __init__(self, url, params=None):
        self.url = url
        self.params = params

    def get(self, duration=None):
        self._sleep(duration)
        print("going to:", self.url)

        return requests.get(self.url, params=self.params)

    def _sleep(self, duration):
        zzz = duration if duration else random.randrange(3, 15)
        print("sleeping:", zzz)
        time.sleep(zzz)
