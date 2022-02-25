# -*- coding: utf-8 -*-

import requests

## 原始的方式请求数据
# res = requests.get("http://127.0.0.1:8000/server/")
# print(res.text)


#### 第一种方式
# token = 'xdrfdsfsdf'
# res = requests.get("http://127.0.0.1:8000/server/", headers={"token": token})
# print(res.text)


#### 第二种方式

token = 'xdrfdsfsdf'

import time

client_time = time.time()
tmp = "%s|%s" % (token, client_time)
import hashlib

m = hashlib.md5()
m.update(bytes(tmp, encoding='utf-8'))
res = m.hexdigest()

client_md5_token = "%s|%s" % (res, client_time)
res = requests.get("http://127.0.0.1:8000/server/", headers={"token": client_md5_token})

print(res.text)
