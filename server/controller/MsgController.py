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
class AddHandler(AuthenHandler):
	def post(self):
		title = self.get_argument('title')
		content = self.get_argument('content')
		user = self.get_user()
		self.write(MsgDao.add(title,content,user))

class DeleHandler(AuthenHandler):
	def get(self):
		msg_id = self.get_argument('msg_id')
		print msg_id
		user = self.get_user()
		self.write(MsgDao.delete(msg_id,user))
class ListHandler(AuthenHandler):
	def get(self):
		self.write(self.render_template('msg/list'))
	def post(self):
		user = self.get_user()
		response = RESPONSE.LIST_SUCCESS
		response['data'] = MsgDao.list(user)
		self.write(response)

		
		
		
handlers = [
	(r"/msg/push", PushHandler),
	(r"/msg/add", AddHandler),
	(r"/msg/delete", DeleHandler),
	(r"/msg/list", ListHandler),
]