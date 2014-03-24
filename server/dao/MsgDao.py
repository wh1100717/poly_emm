#!/usr/bin/env python
# -*- coding: utf-8 -*-

from util import MongoUtil
from dao import UserDao

MsgCollection = MongoUtil.db.msg

def pull_list(token, did, last_msgid):
	user = UserDao.get_user_by_token(token)
	if not user: return {'status':0, 'desc':'wrong token'}
	device_msgs = MsgCollection.find_one({'did':did})
	if not device_msgs: return {'status':0, 'desc':'no msg'}
	pull_msgs = []
	for msg in device_msgs:
		if msg['msgid'] > last_msgid:
			pull_msgs.push({
				'msgid':msg['msgid'],
				'title':msg['title'],
				'time':msg['time']
				})
	if pull_msgs == []: return {'status':0, 'desc':'no new msg'}
	return {'status':1, 'data': pull_msgs}

def pull(token, did, msgid):
	user = UserDao.get_user_by_token(token)
	if not user: return {'status':0, 'desc':'wrong token'}
	device_msgs = MsgCollection.find_one({'did':did})
	if not device_msgs: return {'status':0, 'desc':'no msg'}
	for msg in device_msgs:
		if msg['msgid'] == msgid:
			return {'status':1, 'data':{'title':msg['title'],'content':msg['content']}}
	return {'status':0, 'desc':'no specific msg'}

