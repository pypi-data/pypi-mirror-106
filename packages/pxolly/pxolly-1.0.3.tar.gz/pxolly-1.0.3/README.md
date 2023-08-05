# pxolly API Wrapper
![PyPI](https://img.shields.io/pypi/v/pxolly)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pxolly)
![GitHub](https://img.shields.io/github/license/lordralinc/pxolly_api)

## Установка 
```shell
pip install -U pxolly
```
или
```shell
pip install -U https://github.com/lordralinc/pxolly_api/archive/master.zip
```
## Получение токена
N/A

## Использование
```python
from pxolly import PxollyAPI

api = PxollyAPI("access_token")
api.acc.get_info()
api.make_request("method", {"foo": "bar"})
await api.make_request_async("method", {"foo": "bar"})
```

## Методы
N/A