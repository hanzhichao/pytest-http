import logging
import requests
import pytest

DEFAULT_TIMEOUT = 30


class HTTP(object):
    def __init__(self, base_url: str = None, **kwargs):
        self.base_url = base_url
        self.session = requests.Session()
        for key, value in kwargs.items():
            setattr(self.session, key, value)
        #
        # self.session.headers = headers or {}
        # self.session.params = params or {}
        # self.session.timeout = timeout or DEFAULT_TIMEOUT
        # self.session.proxies = proxies

    def request(self, method, url, **kwargs):
        if self.base_url and not url.startswith('http'):
            url = '%s/%s' % (self.base_url.lstrip('/'), url.rstrip('/'))

        logging.debug(f"Request: GET {url} {kwargs}")
        res = self.session.request(method, url, **kwargs)
        logging.debug(f"Response: {res.text}")
        return res

    def get(self, url, **kwargs):
        return self.request('GET', url, **kwargs)

    def post(self, url, **kwargs):
        return self.request('POST', url, **kwargs)

    def put(self, url, **kwargs):
        return self.request('PUT', url, **kwargs)

    def delete(self, url, **kwargs):
        return self.request('DELETE', url, **kwargs)

    def options(self, url, **kwargs):
        return self.request('OPTIONS', url, **kwargs)


@pytest.fixture
def base_url(request):
    config = request.config
    return config.getoption('--base-url') or config.getini('base_url')


@pytest.fixture
def http_default_timeout():
    return None


@pytest.fixture
def http_default_headers():
    return None


@pytest.fixture
def http_default_params():
    return None


@pytest.fixture
def http_default_proxies():
    return None


@pytest.fixture
def http(base_url, http_default_headers, http_default_params, http_default_timeout, http_default_proxies):
    return HTTP(base_url,
                headers=http_default_headers,
                params=http_default_params,
                timeout=http_default_timeout,
                proxies=http_default_proxies)
