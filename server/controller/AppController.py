#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from base import *
from dao import AppDao
from util import StringUtil

class UpdateHandler(BaseHandler):
	def get(self):
		did = self.get_argument('did')
		token = self.get_argument('token')
		data = StringUtil.string2dict(self.get_argument('data'))
		apps = data['apps']
		result = AppDao.update(token,did,apps)
		self.write(result)

class ListHandler(AuthenHandler):
	def get(self):
		did = self.get_argument('did')
		user = self.get_user()
		app_list = AppDao.list(did, user)

handlers = [
	(r"/app/list", ListHandler),
	(r"/app/update", UpdateHandler),
]