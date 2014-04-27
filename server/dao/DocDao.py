#!/usr/bin/env python
# -*- coding: utf-8 -*-

from util import MongoUtil
from dao import UserDao
from dao import DeviceDao
from status import *
import time
import os

DocCollection = MongoUtil.db.doc
UserCollection = MongoUtil.db.user

def upload(doc_name,upload_path,user):
	doc = {
		'doc_id': MongoUtil.getNextSequence('doc_id'),
		'doc_name': doc_name,
		'upload_path': upload_path+'/'+doc_name,
		'tid': user['tid'],
		'time': time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
			
	}
	DocCollection.insert(doc)
	return RESPONSE.SUCCESS
def delete(doc_id,user):
	print doc_id
	doc_path = DocCollection.find_one({'doc_id':int(doc_id)})['upload_path']
	print doc_path
	# doc_path = DocCollection.find_one({'doc_id':doc_id})['upload_path']
	# print doc_path
	os.remove(doc_path)
	DocCollection.remove({'doc_id':int(doc_id)})
	return RESPONSE.SUCCESS
def list(user):
	tid = user['tid']
	doc_lists = DocCollection.find({'tid':tid})
	data = []
	for doc_list in doc_lists:
		doc_info = {}
		doc_info['doc_id'] = doc_list['doc_id']
		doc_info['doc_name'] = doc_list['doc_name']
		doc_info['time'] = doc_list['time']
		data.append(doc_info)
	
	return data

# def push(doc_id,device_lists,user):
# 	time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
# 	msg = MsgCollection.find_one({'msg_id',msg_id})
# 	msg['msg_history'] = [{'time':time,'device_lists':device_lists}]
# 	MsgCollection.update({'msg_id':msg_id},msg)
# 	cids=[]
# 	for device in user['devices']:
# 		if device['did'] in device_lists:
# 			device['pull_info'] = {'type':'msg','msg_id':msg_id}
# 			cids.append(device['cid'])
# 	UserCollection.update({'tid':user['tid']},user)
# 	return cids