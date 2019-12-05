# pytest-http

Pytest发送HTTP请求

---

### 如何使用

1. 安装 `pytest-http`

使用pip从github安装
```
pip install git+https://github.com/hanzhichao/pytest-http
```

2. 使用fixture函数: http
```
def test_a(http):  # 所有数据
    res = http.get('https://www.baidu.com')
    print(res.text)  

```

---

- Email: <a href="mailto:superhin@126.com?Subject=Pytest%20Email" target="_blank">`superhin@126.com`</a> 
- Blog: <a href="https://www.cnblogs.com/superhin/" target="_blank">`博客园 韩志超`</a>
- 简书: <a href="https://www.jianshu.com/u/0115903ded22" target="_blank">`简书 韩志超`</a>

