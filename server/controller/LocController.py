#!/usr/bin/env python
# -*- coding: utf-8 -*-

from base import *
from dao import LocDao
import time

class UpdateHandler(BaseHandler):
	def get(self):
		did = self.get_argument('did')
		token = self.get_argument('token')
		data = StringUtil.string2dict(self.get_argument('data'))
		loc_info = data['loc_info']
		loc_info['timestamp'] = time.time()
		result = LocDao.update(token,did,loc_info)
		self.write(result)

handlers = [
	(r"/loc/update", UpdateHandler),
]