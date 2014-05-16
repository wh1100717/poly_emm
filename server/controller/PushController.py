#!/usr/bin/env python
# -*- coding: utf-8 -*-
from base import *
from status import *
from dao import PushDao
from util import NewIgetuiUtil
class PushHandler(AuthenHandler):
	def post(self):
		user = self.get_user()
		push_type = self.get_argument('type')
		push_type_id = self.get_argument('push_type_id')
		device_lists = self.get_arguments('check_list')
		print push_type
		print push_type_id
		print device_lists
		cids = PushDao.save_info(push_type,push_type_id,device_lists,user)
		print cids
		NewIgetuiUtil.pushMessageToList(cids)
		
		# ret = ret.replace("=",":")
		# return ret
		self.write(RESPONSE.SUCCESS)

class PushDeviceHandler(AuthenHandler):
# list devices
	def get(self):
		user = self.get_user()
		response = RESPONSE.LIST_SUCCESS
		response['data'] = PushDao.list(user)
		# print response
		self.write(response)

handlers = [
	(r"/push/send",PushHandler),
	(r"/push/devices",PushDeviceHandler),
	
	
]
