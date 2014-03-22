#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
UserController:			处理用户请求
	/user/register		#注册账户
	/user/login 		#登陆
	/user/logout 		#登出
'''

import hashlib
from base import *
from dao import UserDao


class RegisterHandler(BaseHandler):
	def post(self):
		email = self.get_argument('email')
		username = self.get_argument('username')
		password = self.get_argument('password')
		password_confirm = self.get_argument('password_confirm')
		accept = self.get_argument('accept', default='off')

		if password != password_confirm:
			self.write('diff_password')
			return

		result = UserDao.register(email, username, password)
		self.write(result)

class LoginHandler(BaseHandler):
	def get(self):
		self.redirect("/") if self.get_user() else self.write(self.render_template('user/login'))			

	def post(self):
		username = self.get_argument('username')
		password = self.get_argument('password')
		remember_me = self.get_argument('remember_me',default='off')

		user = UserDao.get_user(username)
		if not user:
			self.write('invalid user')
		elif hashlib.md5(password).hexdigest() != user['password']:
			self.write('invalid password')
		else:
			self.set_secure_cookie("user",username)
			self.write('success')

class LogoutHandler(BaseHandler):
	def get(self):
		self.set_secure_cookie("user","")
		self.redirect("/user/login")

handlers = [
	(r"/user/register", RegisterHandler),
	(r"/user/login", LoginHandler),
	(r"/user/logout", LogoutHandler),
]