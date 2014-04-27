#!/usr/bin/env python
# -*- coding: utf-8 -*-

from base import *
from status import *
from dao import DocDao
from util import IgetuiUtil

class DocsHandler(AuthenHandler):
	#upload docs
	def post(self):
		user = self.get_user()
		# upload_path=os.path.join(os.path.dirname(__file__),'files')  #文件的暂存路径
		upload_path = os.path.join(os.getcwd(),'files')
		file_metas=self.request.files['file']    #提取表单中‘name’为‘file’的文件元数据

		for meta in file_metas:
            			doc_name=meta['filename']
            			print doc_name
            			filepath=os.path.join(upload_path,doc_name)
            			print filepath
            			with open(filepath,'wb') as up:      #有些文件需要已二进制的形式存储，实际中可以更改
                			up.write(meta['body'])
                	
		self.write(DocDao.upload(doc_name,upload_path,user))

	#list docs
	def get(self):
		user = self.get_user()
		response = RESPONSE.LIST_SUCCESS
		response['data'] = DocDao.list(user)
		self.write(response)
	
	#Delete docs
	def delete(self,docid):
		user = self.get_user()
		self.write(DocDao.delete(docid,user))

	
		
handlers = [
	# (r"/docs/push", PushHandler),
	(r"/docs", DocsHandler),
	(r"/docs/([1-9]+)", DocsHandler),
]