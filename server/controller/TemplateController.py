#!/usr/bin/env python
# -*- coding: utf-8 -*-
from base import *
from status import *
class DeviceHandler(AuthenHandler):
	def get(self):
		self.write(self.render_template('device/list'))
class MsgHandler(AuthenHandler):
	def get(self):
		self.write(self.render_template('msg/list'))
class DocHandler(AuthenHandler):
	def get(self):
		self.write(self.render_template('doc/list'))

handlers = [
	(r"/html/device", DeviceHandler),
	(r"/html/msg",MsgHandler),
	(r"/html/doc",DocHandler)
]

