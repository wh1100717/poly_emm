#!/usr/bin/env python
# -*- coding: utf-8 -*-

from util import MongoUtil
from dao import UserDao
from dao import DeviceDao
from status import *
import time
import os

AppCollection = MongoUtil.db.app
UserCollection = MongoUtil.db.user

def upload(file_metas,upload_path,user):
	for meta in file_metas:
		app_name=meta['filename']
        filepath=os.path.join(upload_path,app_name)
        with open(filepath,'wb') as up:      #有些文件需要已二进制的形式存储，实际中可以更改
        	up.write(meta['body'])

	app = {
		'app_id': MongoUtil.getNextSequence('app_id'),
		'app_name': app_name,
		'upload_path': upload_path+'/'+app_name,
		'tid': user['tid'],
		'time': time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
			
	}
	AppCollection.insert(app)
	return RESPONSE.SUCCESS
def delete(app_id,user):
	print app_id
	app_path = AppCollection.find_one({'app_id':int(app_id)})['upload_path']
	print app_path
	# doc_path = DocCollection.find_one({'doc_id':doc_id})['upload_path']
	# print doc_path
	os.remove(app_path)
	AppCollection.remove({'app_id':int(app_id)})
	return RESPONSE.SUCCESS
def list(user):
	tid = user['tid']
	app_lists = AppCollection.find({'tid':tid})
	data = []
	for app_list in app_lists:
		app_info = {}
		app_info['app_id'] = app_list['app_id']
		app_info['app_name'] = app_list['app_name']
		app_info['time'] = app_list['time']
		data.append(app_info)
	
	return data
