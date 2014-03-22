#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
UserController:			处理用户请求
	/user/register		#注册账户
	/user/login 		#登陆
	/user/logout 		#登出
'''

from base import *

class RegisterHandler(BaseHandler):
	def get(self):
		self.write(self.render_template('user/register'))

	def post(self):
		self.write('success_post')

class LoginHandler(BaseHandler):
	def get(self):
		self.write(self.render_template('user/login'))

class LogoutHandler(BaseHandler):
	def get(self):
		self.write('success_logout')


handlers = [
	(r"/user/register", RegisterHandler),
	(r"/user/login", LoginHandler),
	(r"/user/logout", LogoutHandler),
]