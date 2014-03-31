#!/usr/bin/env python
# -*- coding: utf-8 -*-

from base import *
from status import *
from dao import MsgDao
from util import IgetuiUtil

class PushHandler(AuthenHandler):
	def post(self):
		title = self.get_argument('title')
		content = self.get_argument('content')
		did = self.get_argument('did')
		user = self.get_user()
		cid = MsgDao.push(title,content,did,user)
		if cid == 0:
			self.write(RESPONSE.FAIL)
			return
		template = IgetuiUtil.generateTrasmissionTemplate(transmissionContent = {'type':1})
		response = IgetuiUtil.pushMessageToSingle(cid=cid,template=template)
		print response
		self.write('123')

handlers = [
	(r"/msg/push", PushHandler),
]