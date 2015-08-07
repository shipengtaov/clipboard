A Simple Clipboard
=======================

**获取 key 的内容:**

HTTP GET 请求: 

`http://<ip>:<port>/key?passwd=yourpassword`

**存储内容到 key:**

HTTP POST 请求: 

`http://<ip>:<port>/key`

payload={"passwd": "your password", "data": "your data"}

**Requirements:**

* tornado

* redis

License:
========

MIT