#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
DeviceController:	处理设备请求
	/device/...
'''

from base import *
from dao import DeviceDao


class RegisterHistoryHandler(BaseHandler):
	def get(self):
		result = '''
			{
				"2014-02-25": "{'crawled': '19009', 'update': '290', 'new': '8'}",
				"2014-02-24": "{'crawled': '18692', 'update': '28', 'new': '0'}",
				"2014-02-27": "{'crawled': '18249', 'update': '242', 'new': '12'}",
				"2014-02-26": "{'crawled': '18667', 'update': '159', 'new': '10'}",
				"2014-02-21": "{'crawled': '16360', 'update': '2114', 'new': '14174'}",
				"2014-02-20": "{'crawled': '8164', 'update': '383', 'new': '7545'}",
				"2014-02-23": "{'crawled': '18676', 'update': '824', 'new': '1004'}",
				"2014-02-22": "{'crawled': '18586', 'update': '4857', 'new': '13605'}"
			}
		'''
		self.write(result)

class StatisticsHandler(BaseHandler):
	def get(self):
		data = {
			'last7_lost_controll_devices': 32,
			'root_devices': 11,
			'last7_noncompliance_devices': 8,
			'last7_new_devices': 6998,
			'china_unicom_devices': 7,
			'china_mobile_devices': 6251,
			'china_telecom_devices': 666,
			'device_amount': 22,
			'user_amount': 2123,
			'app_amount': 1205,
		}
		self.write(data)

class DeviceActiveListHandler(BaseHandler):
	def get(self):
		data = {
			"total":"5100",
			"max":"10000",
			"data":[
				{
					'device_name':'iphone-7823',
					'owner_name':'Eric',
					'sn_number':'234-2342-343',
					'device_type':'iphone4',
					'platform':'ios',
					'registion_time':1393827011000,
					'last_update_time':1393828011000,
				},
				{
					'device_name':'iphone-7823',
					'owner_name':'Eric',
					'sn_number':'234-2342-343',
					'device_type':'iphone4',
					'platform':'ios',
					'registion_time':1393827011000,
					'last_update_time':1393828011000,
				}
			]
		}
		self.write(data)

class RegisterListHandler(BaseHandler):
	def get(self):
		data = {
			'data':DeviceDao.register_list(self.get_user())
		}
		self.write(data)

class DeviceAddHandler(BaseHandler):
	def post(self):
		uid = self.get_argument('uid')
		owner = self.get_argument('owner')
		user = self.get_user()
		if DeviceDao.exist(uid,owner,user):
			result = 'device is exist'
		else:
			result = DeviceDao.add(uid,owner,user)
		self.write(result)

class EnrollHandler(BaseHandler):
	def get(self):
		uid = self.get_argument('uid')
		active_code = self.get_argument('active_code')
		tanent_id = self.get_argument('tanent_id')
		self.write(DeviceDao.enroll(uid, active_code, tanent_id))

	def post(self):
		uid = self.get_argument('uid')
		active_code = self.get_argument('active_code')
		tanent_id = self.get_argument('tanent_id')
		self.write(DeviceDao.enroll(uid, active_code, tanent_id))

class UpdateHandler(BaseHandler):
	def get(self):
		token = self.get_argument('token')
		uid = self.get_argument('uid')
		did = self.get_argument('did')
		cid = self.get_argument('cid')
		imei = self.get_argument('imei')
		self.write(DeviceDao.update(token,uid,did,cid,imei))

class ConfigHandler(BaseHandler):
	def get(self):
		did = self.get_argument('did')
		token = self.get_argument('token')
		result = DeviceDao.config(token,did)
		self.write(result)


handlers = [
	(r"/device/register_history", RegisterHistoryHandler),
	(r"/device/statistics", StatisticsHandler),
	(r"/device/register/list", RegisterListHandler),
	(r"/device/active/list",DeviceActiveListHandler),
	(r"/device/add",DeviceAddHandler),
	(r"/device/enroll", EnrollHandler),
	(r"/device/update", UpdateHandler),
	(r"/device/config", ConfigHandler),
]
