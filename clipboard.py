#!/usr/bin/env python
# -*- coding: utf-8 -*-

from hashlib import sha1

import redis
import tornado.ioloop
import tornado.web

import config

r = redis.StrictRedis(**config.redis_conf)

def check_passwd(fn):
    def wrapper(self, *args, **kwargs):
        passwd = self.get_argument('passwd', None)
        if passwd not in config.passwds:
            self.set_status(401)
            self.write('wrong passwd')
            raise tornado.web.Finish()
        return fn(self, *args, **kwargs)
    return wrapper

class ClipboardHandler(tornado.web.RequestHandler):
    @check_passwd
    def get(self, key):
        passwd_hash = self.hash_passwd()

        val = r.hget(passwd_hash, key)
        if val == None:
            val = ''
        self.write(val)

    @check_passwd
    def post(self, key):
        passwd_hash = self.hash_passwd()

        data = self.get_argument('data', '')
        if config.data_max_len>0 and len(data)>config.data_max_len:
            data = data[:config.data_max_len]
        r.hset(passwd_hash, key, data)
        if config.ttl >0:
            r.expire(passwd_hash, config.ttl)
        self.write('ok')

    def hash_passwd(self):
        passwd = self.get_argument('passwd')
        return sha1(passwd).hexdigest()

def main():
    application = tornado.web.Application([
        (r"/(.*)", ClipboardHandler)
    ])
    application.listen(config.listen)
    tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
    main()
