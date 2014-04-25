#!/usr/bin/env python
# -*- coding: utf-8 -*-

from base import *
from status import *
from dao import MsgDao
from util import IgetuiUtil

# class PushHandler(AuthenHandler):
# 	def post(self):
# 		title = self.get_argument('title')
# 		content = self.get_argument('content')
# 		did = self.get_argument('did')
# 		user = self.get_user()
# 		cid = MsgDao.push(title,content,did,user)
# 		if cid == 0:
# 			self.write(RESPONSE.FAIL)
# 			return
# 		template = IgetuiUtil.generateTrasmissionTemplate(transmissionContent = {'type':1})
# 		response = IgetuiUtil.pushMessageToSingle(cid=cid,template=template)
# 		print response
# 		self.write('123')
class MsgsHandler(AuthenHandler):
	#Add Msg
	def post(self):
		title = self.get_argument('title')
		content = self.get_argument('content')
		user = self.get_user()
		self.write(MsgDao.add(title,content,user))

	#list Msg
	def get(self):
		user = self.get_user()
		response = RESPONSE.LIST_SUCCESS
		response['data'] = MsgDao.list(user)
		self.write(response)
	
	#Delete Msg
	def delete(self,msgid):
		user = self.get_user()
		self.write(MsgDao.delete(msgid,user))


class PushHandler(AuthenHandler):
	def post(self):
		msg_id = self.get_argument('msg_id')
		device_lists = self.get_argument('device_lists')
		user = self.get_user()
		cids = MsgDao.push(msg_id,device_lists,user)
		template = IgetuiUtil.generateTrasmissionTemplate(transmissionContent = {'type':1})
		response = IgetuiUtil.pushMessageToSingle(cidList=cids,template=template)
		self.write(response)

		
		
		
handlers = [
	(r"/msg/push", PushHandler),
	(r"/msgs", MsgsHandler),
	(r"/msgs/([1-9]+)", MsgsHandler),
]