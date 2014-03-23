#!/usr/bin/env python
# -*- coding: utf-8 -*-
from util import MongoUtil
from util import StringUtil

DeviceCollection = MongoUtil.db.user

#添加设备
def device_add(uid,owner,user):	
	device = {
		'uid':uid,
		'active_code':StringUtil.active_code_generator(),
		'active':False,
		'owner':owner
	}
	if user.has_key('device'):
		user['device'].append(device)
	else:
		user['device'] = [device]
	DeviceCollection.update({'user_name':user['user_name']},user)
	return 'success'

#判断设备是否存在
def dev_exist(uid,owner,user):
	if not user.has_key('device'): return False
	for device in user['device']:
		if device.has_key('uid') and device['uid'] == uid:
			return True
	return False