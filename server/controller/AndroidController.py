#!/usr/bin/env python
# -*- coding: utf-8 -*-

from base import *
from dao import AndroidDao


class EnrollHandler(BaseHandler):
	'''设备登记请求
		paras:
			tid:			user的唯一标识
			active_code:	激活码
			phone:			手机号
		response:
			status:			1表示成功
			token:			用户token，用来做权限验证
	'''
	def get(self):
		tid = self.get_argument('tid')
		active_code = self.get_argument('active_code')
		phone = self.get_argument('phone')
		self.write(AndroidDao.enroll(tid, active_code, phone))

	def post(self):
		tid = self.get_argument('tid')
		active_code = self.get_argument('active_code')
		phone = self.get_argument('phone')
		self.write(AndroidDao.enroll(tid, active_code, phone))

class InitialHandler(BaseHandler):
	'''设备初始化
		paras:
			token:			enroll的时候获取的token密钥
			phone:			手机号
			did:			设备生成的唯一标识
			cid:			用于推送的cid
			imei:			设备唯一标识序列号
		response:
			status:			1表示成功
			initial:		字典格式，表示初始配置信息
	'''
	def get(self):
		token = self.get_argument('token')
		phone = self.get_argument('phone')
		did = self.get_argument('did')
		cid = self.get_argument('cid')
		imei = self.get_argument('did')
		self.write(AndroidDao.initial(token,phone,did,cid,imei))

class PullHandler(BaseHandler):
	'''设备获取数据
		paras:
			token:			enroll的时候获取的token密钥
			did:			设备生成的唯一标识
		response:
			status:			1表示成功
			data:			字典格式，包含了server希望设备获取的所有数据
	'''
	def get(self):
		token = self.get_argument('token')
		did = self.get_argument('did')
		self.write(AndroidDao.pull(token,did))

class RespHandler(BaseHandler):
	'''返回获取状态
		paras:
			token:			enroll的时候获取的token密钥
			did:			设备生成的唯一标识
			status:			1表示成功
		response:
			status:			1表示成功
	'''
	def get(self):
		token = self.get_argument('token')
		did = self.get_argument('did')
		status = self.get_argument('status')
		if status == 1:
			self.write(AndroidDao.resp(token,did))
		else:
			#TODO 需要根据具体的错误状态信息来进行实际业务逻辑
			pass


handlers = [
	(r"/android/enroll", EnrollHandler),
	(r"/android/initial", InitialHandler),
	(r"/android/pull", PullHandler),
	(r"/android/resp", RespHandler),
]



