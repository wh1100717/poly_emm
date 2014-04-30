#!/usr/bin/env python
# -*- coding: utf-8 -*-

from base import *
from status import *
from dao import PolicyDao
from util import IgetuiUtil
#添加策略
class PoliciesHandler(AuthenHandler):
	#add policy
	def post(self):
		policy_id = self.get_argument('policy_id')
		print policy_id
		policy_name = self.get_argument('policy_name')
		platform = self.get_argument('platform')
		policy_content = self.get_argument('content')
		user = self.get_user()
		self.write(PolicyDao.add(policy_id,policy_name,policy_content,platform,user))

	#list policy
	def get(self):
		user = self.get_user()
		response = RESPONSE.LIST_SUCCESS
		response['data'] = PolicyDao.list(user)
		self.write(response)

	#edit policy
	def put(self,policyid):
		print "============"
		# policy_name = self.get_argument('policy_name')
		# policy_content = self.get_argument('policy_content')
		user = self.get_user()
		self.write(PolicyDao.edit(policyid,user))

	#delete policy
	def delete(self,policyid):
		user = self.get_user()
		self.write(PolicyDao.delete(policyid,user))

#推送策略
class PushHandler(AuthenHandler):
	def post(self):
		policy_id = self.get_argument('policy_id')
		device_lists = self.get_argument('device_lists')
		user = self.get_user()
		self.write(PolicyDao.push(policy_id,device_lists,user))

# class EditHandler(AuthenHandler):
# 	def get(self):
# 		# policy_id = self.get_argument('policy_id')
# 		# response = RESPONSE.LIST_SUCCESS
# 		# response['data'] = PolicyDao.detail(policy_id)
# 		# self.write(response)
# 		user = self.get_user()
# 		response = RESPONSE.LIST_SUCCESS
# 		response['data'] = PolicyDao.detail(user)
# 		self.write(response)

handlers = [
	(r"/policies", PoliciesHandler),
	(r"/policies/([1-9]+)", PoliciesHandler),
	# (r"/policies/detail/([1-9]+)",EditHandler),
	
]