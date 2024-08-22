# pytest-http

![Languate - Python](https://img.shields.io/badge/language-python-blue.svg)
![PyPI - License](https://img.shields.io/pypi/l/pytest-owner)
![PyPI](https://img.shields.io/pypi/v/pytest-owner)
![PyPI - Downloads](https://img.shields.io/pypi/dm/pytest-owner)

Pytest发送HTTP请求

---

### 如何使用

1. 安装 `pytest-http`

使用pip从github安装

```sh
pip install pytest-http
```

2. 使用Fixture函数: http

```python
def test_get(http):  # 所有数据
    res = http.get('https://httpbin.org/get?a=1&b=2')
    print(res.text)
```

支持base_url配置

```python
import pytest


@pytest.fixture
def base_url():
    # you can use pytest-base-url instead
    return 'https://httpbin.org'


def test_get(http):  # 所有数据
    res = http.get('/get?a=1&b=2')
    print(res.text)

def test_post(http):  # 所有数据
    res = http.get('/post', data=dict(a=1, b=2))
    print(res.text)
```

3. 其他可用配置

```python
import pytest


@pytest.fixture
def http_default_timeout():
    return 10


@pytest.fixture
def http_default_headers():
    return {'Authorization': 'Bearer xxx'}


@pytest.fixture
def http_default_params():
    return {}


@pytest.fixture
def http_default_proxies():
    return {}
```

---

- Email: <a href="mailto:superhin@126.com?Subject=Pytest%20Email" target="_blank">`superhin@126.com`</a>
- Blog: <a href="https://www.cnblogs.com/superhin/" target="_blank">`博客园 韩志超`</a>
- 简书: <a href="https://www.jianshu.com/u/0115903ded22" target="_blank">`简书 韩志超`</a>

