import logging
import requests
import pytest

TIMEOUT = 30


class HTTP(object):
    def __init__(self, base_url=None):
        self.session = requests.session()
        self.base_url = base_url

    def request(self, method, url, **kwargs):
        url = self.base_url + url if self.base_url else url
        kwargs.setdefault('timeout', TIMEOUT)
        logging.debug(f"Request: GET {url} {kwargs}")
        res = self.session.request(method, url, **kwargs)
        logging.debug(f"Response: {res.text}")
        return res

    def get(self, url, **kwargs):
        return self.request('get', url, **kwargs)

    def post(self, url, **kwargs):
        return self.request('post', url, **kwargs)


@pytest.fixture(scope='session')
def http():
    return HTTP()
