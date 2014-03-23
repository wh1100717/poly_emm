#!/usr/bin/env python
# -*- coding: utf-8 -*-
from util import MongoUtil
from util import StringUtil
import time

DeviceCollection = MongoUtil.db.user

#添加设备
def add(uid,owner,user):	
	device = {
		'uid':uid,
		'active_code':StringUtil.active_code_generator(),
		'active':False,
		'owner':owner,
		'time':time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
	}
	if user.has_key('device'):
		user['device'].append(device)
	else:
		user['device'] = [device]
	DeviceCollection.update({'user_name':user['user_name']},user)
	return 'success'


#判断设备是否存在
def exist(uid,owner,user):
	if not user.has_key('device'): return False
	for device in user['device']:
		if device.has_key('uid') and device['uid'] == uid:
			return True
	return False

#获取注册列表
def register_list(user):
	if not user.has_key('device'): return []
	devices = user['device']
	device_register_lists=[]
	for device in devices:
		device_register_list={
			'uid':device['uid'],
			'owner':device['owner'],
			'active_code':device['active_code'],
			'active':device['active'],
			'time':device['time']
		}
		device_register_lists.append(device_register_list)
	return device_register_lists