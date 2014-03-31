#!/usr/bin/env python
# -*- coding: utf-8 -*-
import platform
import os
import sys
reload(sys)

pwd = os.getcwd()
if platform.system().lower() == 'windows':
	pwd += '\\sdk'
	sys.setdefaultencoding('gbk')
else:
	pwd += '/sdk'
	sys.setdefaultencoding('utf-8')
sys.path.append(pwd)

import tornado.ioloop
import tornado.web
import settings
import handler



application = tornado.web.Application(handler.handlers, **settings.__server_config__)

if __name__ == "__main__":
	application.listen(settings.__server_port__)
	tornado.ioloop.IOLoop.instance().start()
