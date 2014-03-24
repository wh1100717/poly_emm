#!/usr/bin/env python
# -*- coding: utf-8 -*-

from base import *
from dao import LocDao
import time

class UpdateHandler(BaseHandler):
	def get(self):
		uid = self.get_argument('uid')
		did = self.get_argument('did')
		token = self.get_argument('token')
		loc_mode = self.get_argument('loc_mode')
		loc_interval = self.get_argument('loc_interval')
		loc_lat = self.get_argument('loc_lat')
		loc_long = self.get_argument('loc_long')
		loc_info = {
			'loc_mode':loc_mode,
			'loc_interval':loc_interval,
			'loc_lat':loc_lat,
			'loc_long':loc_long,
			'timestamp':time.time()
		}

		result = LocDao.update(token,uid,did,loc_info)
		self.write(result)

handlers = [
	(r"/loc/update", UpdateHandler),
]