#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from base import *
from dao import AppDao
from util import StringUtil

class UpdateHandler(BaseHandler):
	def get(self):
		uid = self.get_argument('uid')
		did = self.get_argument('did')
		token = self.get_argument('token')
		data = StringUtil.string2dict(self.get_argument('data'))
		app_list = data['app_list']
		result = AppDao.update(token,uid,did,app_list)
		self.write(result)

handlers = [
	(r"/app/update", UpdateHandler),
]