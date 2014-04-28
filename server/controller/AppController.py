#!/usr/bin/env python
# -*- coding: utf-8 -*-

from base import *
from status import *
from dao import AppDao
from util import IgetuiUtil

class AppsHandler(AuthenHandler):
	#upload apps
	def post(self):
		user = self.get_user()
		# upload_path=os.path.join(os.path.dirname(__file__),'files')  #文件的暂存路径
		upload_path = os.path.join(os.getcwd(),'apps')
		if not os.path.isdir(upload_path):
			os.makedirs(upload_path)
		file_metas=self.request.files['file']    #提取表单中‘name’为‘file’的文件元数据

		self.write(AppDao.upload(file_metas,upload_path,user))

	#list apps
	def get(self):
		user = self.get_user()
		response = RESPONSE.LIST_SUCCESS
		response['data'] = AppDao.list(user)
		self.write(response)
	
	#Delete apps
	def delete(self,appid):
		user = self.get_user()
		self.write(AppDao.delete(appid,user))

	
		
handlers = [
	# (r"/docs/push", PushHandler),
	(r"/apps", AppsHandler),
	(r"/apps/([1-9]+)", AppsHandler),
]