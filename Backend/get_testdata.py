# -*- coding:utf-8 -*-
import tornado.web
import subprocess

class getdata(tornado.web.RequestHandler):
    def post(self):
        # todo
        self.write("getdata")

