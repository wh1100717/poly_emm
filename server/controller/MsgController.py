#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dao import MsgDao



class PullListHandler(BaseHandler):
	def get(self):
		token = self.get_argument('token')
		did = self.get_argument('did')
		last_msgid = self.get_argument('last_msgid')
		result = MsgDao.pull_list(token,did,last_msgid)
		self.write(result)

class PullHandler(BaseHandler):
	def get(self):
		token = self.get_argument('token')
		did = self.get_argument('did')
		msgid = self.get_argument('msgid')
		result = MsgDao.pull(token,did,msgid)
		self.write(result)


handlers = [
	(r"/msg/pull_list", PullListHandler),
	(r"/msg/pull", PullHandler),
]