#!/usr/bin/env python
# -*- coding: utf-8 -*-
from base import *
from status import *
class DeviceHandler(AuthenHandler):
	def get(self):
		self.write(self.render_template('device/list'))
handlers = [
	(r"/html/device", DeviceHandler)
]
