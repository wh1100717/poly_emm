#!/usr/bin/env python
# -*- coding: utf-8 -*-

from base import *
from dao import PolicyDao
#添加策略
class AddHandler(AuthenHandler):
	def post(self):
		policy_name = self.get_argument('policy_name')
		platform = self.get_argument('platform')
		user = self.get_user()
		self.write(PolicyDao.add(policy_name,platform,user))
#编辑策略
class EditHandler(AuthenHandler):
	def post(self):
		policy_id = self.get_argument('policy_id')
		policy_content = self.get_argument('policy_content')
		user = self.get_user()
		self.write(PolicyDao.edit(policy_id,policy_content,user))
#删除策略
class DeleteHandler(AuthenHandler):
	def post(self):
		policy_id = self.get_argument('policy_id')
		user = self.get_user()
		self.write(PolicyDao.delete(policy_id,user))
#推送策略
class PushHandler(AuthenHandler):
	def post(self):
		policy_id = self.get_argument('policy_id')
		device_lists = self.get_argument('device_lists')
		user = self.get_user()
		self.write(PolicyDao.push(policy_id,device_lists,user))
class ListHandler(AuthenHandler):
	def get(self):
		self.write(self.render_template('policy/list'))
	def post(self):
		user = self.get_user()
		response = RESPONSE.LIST_SUCCESS
		response['data'] = PolicyDao.list(user)
		self.write(response)
handlers = [
	(r"/policy/add", AddHandler),
	(r"/policy/edit", EditHandler),
	(r"/policy/delete", DeleteHandler),
	(r"/policy/list", ListHandler),
	(r"/policy/push", PushHandler),
	
]