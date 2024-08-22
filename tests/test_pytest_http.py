import pytest


@pytest.fixture
def base_url():
    return 'http://httpbin.org'


def test_httpbin_get(http):
    resp = http.get('/get?a=1&b=2')
    print(resp.text)


def test_b():
    pass
