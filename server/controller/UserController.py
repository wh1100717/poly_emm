#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
UserController:			处理用户请求
	/user/register		#注册账户
	/user/login 		#登陆
	/user/logout 		#登出
'''

import hashlib
import time
from base import *
from status import *
from dao import UserDao
from util import StringUtil


class RegisterHandler(BaseHandler):
	def post(self):
		'''用户注册
		paras:
			*	email_or_phone: 	用户可以输入自己的手机号或者邮箱用来注册
			*	user_name:			用来显示用户名称，不唯一
			*	pwd:				用户登录密码
			*	pwd_confirm:		用户登录密码确认
			*	accept:				用户是否接受使用条款
		'''
		email_or_phone = self.get_argument('email_or_phone')
		user_name = self.get_argument('user_name')
		pwd = self.get_argument('pwd')
		
		enroll_type = StringUtil.is_email_or_phone(email_or_phone)
		if enroll_type == 'neither':
			#如果用户输入不是邮箱或者电话号，则注册失败
			self.write(RESPONSE.WRONG_TYPE)
			return
		elif enroll_type == 'email':
			#如果email已经注册，则注册失败
			if UserDao.get_user_by_email(email_or_phone):
				self.write(RESPONSE.EMAIL_EXIST)
				return
		else:
			#如果手机号已经注册，则注册失败
			if UserDao.get_user_by_phone(email_or_phone):
				self.write(RESPONSE.PHONE_EXIST)
				return
		#进行用户注册流程
		UserDao.register(email_or_phone, enroll_type, user_name, pwd)
		self.write(RESPONSE.SUCCESS)

class LoginHandler(BaseHandler):
	def get(self):
		'''登陆页面
		如果用户已经登陆则跳转到首页，否则返回登陆页
		'''
		self.redirect("/") if self.get_user() else self.write(self.render_template('user/login'))			

	def post(self):
		'''登陆请求
		paras:
			*	email_or_phone 		用户可以输入手机号或者邮箱来进行登陆
			*	pwd 				登陆密码
			*	remember_me			是否记住登陆状态(TODO)
		response:

		'''
		email_or_phone = self.get_argument('email_or_phone')
		pwd = self.get_argument('pwd')
		remember_me = self.get_argument('remember_me',default='off')

		enroll_type = StringUtil.is_email_or_phone(email_or_phone)
		if enroll_type == 'neither':
			#如果用户输入不是邮箱或者电话号，则登陆失败
			self.write(RESPONSE.WRONG_TYPE)
			return
		user = UserDao.get_user_by_email(email_or_phone) if enroll_type == 'email' else UserDao.get_user_by_phone(email_or_phone)
		if not user:
			#如果取不到用户，则登陆失败
			self.write(RESPONSE.WRONG_TYPE)
		elif hashlib.md5(pwd).hexdigest() != user['pwd']:
			#如果密码错误，则登陆失败
			self.write(RESPONSE.INVALID_PASSWORD)
		else:
			self.set_secure_cookie("tid",str(user['tid']))
			self.set_secure_cookie("timestamp", str(time.time()))
			self.write(RESPONSE.SUCCESS)

class LogoutHandler(BaseHandler):
	def get(self):
		self.set_secure_cookie("tid","")
		self.set_secure_cookie("timestamp","")
		self.redirect("/user/login")

handlers = [
	(r"/user/register", RegisterHandler),
	(r"/user/login", LoginHandler),
	(r"/user/logout", LogoutHandler),
]