#!/usr/bin/env python
# -*- coding: utf-8 -*-

from util import MongoUtil
from dao import UserDao
from status import *
import time

MsgCollection = MongoUtil.db.msg

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

def push(title,content,did,user):
	devices = user['devices']
	for device in devices:
		if device.has_key('did') and device['did'] == did:
			if not device.has_key('cid'):
				return {}
			msg = {
				'msg_id': MongoUtil.getNextSequence('msg_id'),
				'title': title,
				'content': content,
				'cid': device['cid'],
				'token': user['token'],
				'time': time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
			}
			MsgCollection.insert(msg)

			if not device.has_key('push_info'):
				device['push_info'] = {}
			if not device['push_info'].has_key('msg'):
				device['push_info']['msg'] = []
			device['push_info']['msg'].append({
				'msg_id': msg['msg_id'],
				'title': msg['title'],
				'time': msg['time']
				})
		return msg['cid']
	return 0


