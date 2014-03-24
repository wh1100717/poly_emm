#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
	
	blacklist/upsert 更新黑名单
	blacklist/del 删除黑名单
	blacklist/get_list 获得黑名单
'''

from base import *
from dao import BlackListDao
#get_list获取黑名单列表
class ListHandler(BaseHandler):
	def get(self):
		token = self.get_argument('token')
		did = self.get_argument('did')
		self.write(BlackListDao.list(token,did))
#添加应用
class InsertAppHandler(AuthenHandler):
	def get(self):
		user = self.get_user()
		did = self.get_argument('did')
		apps = self.get_argument('apps')
		self.write(BlackListDao.app_insert(user,did,apps))
#删除应用
class DeleteAppHandler(AuthenHandler):
	def get(self):
		user = self.get_user()
		did = self.get_argument('did')
		apps = self.get_argument('apps')
		self.write(BlackListDao.delete(user,did,apps))
handlers = [
	(r"/blacklist/insert_app", InsertAppHandler),
	(r"/blacklist/delete_app", DeleteAppHandler),
	(r"/blacklist/List", ListHandler),
]