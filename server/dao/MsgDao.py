#!/usr/bin/env python
# -*- coding: utf-8 -*-

from util import MongoUtil
from dao import UserDao
from dao import DeviceDao
from status import *
import time

MsgCollection = MongoUtil.db.msg
UserCollection = MongoUtil.db.user

# def pull_list(token, did, last_msgid):
# 	user = UserDao.get_user_by_token(token)
# 	if not user: return {'status':0, 'desc':'wrong token'}
# 	device_msgs = MsgCollection.find_one({'did':did})
# 	if not device_msgs: return {'status':0, 'desc':'no msg'}
# 	pull_msgs = []
# 	for msg in device_msgs:
# 		if msg['msgid'] > last_msgid:
# 			pull_msgs.push({
# 				'msgid':msg['msgid'],
# 				'title':msg['title'],
# 				'time':msg['time']
# 				})
# 	if pull_msgs == []: return {'status':0, 'desc':'no new msg'}
# 	return {'status':1, 'data': pull_msgs}

# def pull(token, did, msgid):
# 	user = UserDao.get_user_by_token(token)
# 	if not user: return {'status':0, 'desc':'wrong token'}
# 	device_msgs = MsgCollection.find_one({'did':did})
# 	if not device_msgs: return {'status':0, 'desc':'no msg'}
# 	for msg in device_msgs:
# 		if msg['msgid'] == msgid:
# 			return {'status':1, 'data':{'title':msg['title'],'content':msg['content']}}
# 	return {'status':0, 'desc':'no specific msg'}

# def push(title,content,did,user):
# 	devices = DeviceDao.get_devices_by_user(user)
# 	for device in devices:
# 		if device.has_key('did') and device['did'] == did:
# 			if not device.has_key('cid'):
# 				return {}
# 			msg = {
# 				'msg_id': MongoUtil.getNextSequence('msg_id'),
# 				'title': title,
# 				'content': content,
# 				'cid': device['cid'],
# 				'token': user['token'],
# 				'time': time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
# 			}
# 			MsgCollection.insert(msg)

# 			if not device.has_key('push_info'):
# 				device['push_info'] = {}
# 			if not device['push_info'].has_key('msg'):
# 				device['push_info']['msg'] = []
# 			device['push_info']['msg'].append({
# 				'msg_id': msg['msg_id'],
# 				'title': msg['title'],
# 				'time': msg['time']
# 				})
# 		return msg['cid']
# 	return 0
def add(title,content,user):
	msg = {
		'msg_id': MongoUtil.getNextSequence('msg_id'),
		'title': title,
		'content': content,
		'tid': user['tid'],
		'time': time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
			
	}
	MsgCollection.insert(msg)
	return RESPONSE.SUCCESS
def delete(msg_id,user):

	MsgCollection.remove({'msg_id':int(msg_id)})
	return RESPONSE.SUCCESS
def list(user):
	tid = user['tid']
	msg_lists = MsgCollection.find({'tid':tid})
	data = []
	for msg_list in msg_lists:
		msg_info = {}
		msg_info['msg_id'] = msg_list['msg_id']
		msg_info['title'] = msg_list['title']
		msg_info['content'] = msg_list['content']
		msg_info['time'] = msg_list['time']
		data.append(msg_info)
	
	return data

def push(msg_id,device_lists,user):
	time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
	msg = MsgCollection.find_one({'msg_id',msg_id})
	msg['msg_history'] = [{'time':time,'device_lists':device_lists}]
	MsgCollection.update({'msg_id':msg_id},msg)
	cids=[]
	for device in user['devices']:
		if device['did'] in device_lists:
			device['pull_info'] = {'type':'msg','msg_id':msg_id}
			cids.append(device['cid'])
	UserCollection.update({'tid':user['tid']},user)
	return cids