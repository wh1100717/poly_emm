#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.web
from base import *
from controller import UserController
from controller import DeviceController

handlers = []
'''
UserController:			处理用户请求
	/user/register		#注册账户
	/user/login 		#登陆
	/user/logout 		#登出
'''
handlers += UserController.handlers
'''
DeviceController:	处理设备请求
	/device/...
'''
handlers += DeviceController.handlers

handlers += [(r"^/(.*)$", BaseHandler)]
