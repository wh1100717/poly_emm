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
		user_name = self.get_argument('user_name')
		pwd = self.get_argument('pwd')
		pwd_confirm = self.get_argument('pwd_confirm')
		accept = self.get_argument('accept', default='off')

		if pwd != pwd_confirm:
			self.write('diff_password')
			return

		result = UserDao.register(email, user_name, pwd)
		self.write(result)

class LoginHandler(BaseHandler):
	def get(self):
		self.redirect("/") if self.get_user() else self.write(self.render_template('user/login'))			

	def post(self):
		email = self.get_argument('email')
		pwd = self.get_argument('pwd')
		remember_me = self.get_argument('remember_me',default='off')

		user = UserDao.get_user_by_email(email)
		if not user:
			self.write('invalid email')
		elif hashlib.md5(pwd).hexdigest() != user['pwd']:
			self.write('invalid password')
		else:
			self.set_secure_cookie("email",email)
			self.write('success')

class LogoutHandler(BaseHandler):
	def get(self):
		self.set_secure_cookie("email","")
		self.redirect("/user/login")

handlers = [
	(r"/user/register", RegisterHandler),
	(r"/user/login", LoginHandler),
	(r"/user/logout", LogoutHandler),
]