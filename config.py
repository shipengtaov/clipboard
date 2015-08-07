#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 允许使用的密码
passwds = [
    "passwd",
]

# 每个 passwd 数据过期时间. 0:不限制
ttl = 60*60*24

# 允许存储的最大数据长度. 0:不限制
data_max_len = 5000

redis_conf = {
    "host": "127.0.0.1",
    "port": 6379,
    # "db": 0,
}

listen = 8888
