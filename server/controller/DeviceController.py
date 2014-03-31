#!/usr/bin/env python
# -*- coding: utf-8 -*-
from base import *
from status import *
from dao import DeviceDao

class AddHandler(AuthenHandler):
	def post(self):
		phone = self.get_argument('phone')
		owner = self.get_argument('owner')
		user = self.get_user()
		if DeviceDao.exist_by_phone(phone,user):
			self.write(RESPONSE.DEVICE_EXIST)
			return
		self.write(DeviceDao.add(phone,owner,user))

class ListHandler(AuthenHandler):
	def get(self):
		user = self.get_user()
		response = RESPONSE.LIST_SUCCESS
		response['data'] = DeviceDao.list(user)
		self.write(response)

class DetailHandler(AuthenHandler):
	def get(self):
		did = self.get_argument('did')
		user = self.get_user()
		response = RESPONSE.LIST_SUCCESS
		response['data'] = DeviceDao.detail(did,user)
		self.write(response)

handlers = [
	(r"/device/add",AddHandler),
	(r"/device/list", ListHandler),
	(r"/device/detail", DetailHandler),
]
