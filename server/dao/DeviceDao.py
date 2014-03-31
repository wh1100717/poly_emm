#!/usr/bin/env python
# -*- coding: utf-8 -*-
from util import MongoUtil
from util import StringUtil
from dao import UserDao
from status import *
import time

UserCollection = MongoUtil.db.user

#根据手机号判断设备是否存在
def exist_by_phone(phone,user):
	if not user.has_key('devices'): return False
	for device in user['devices']:
		if device.has_key('phone') and device['phone'] == phone:
			return True
	return False

#根据did判断设备是否存在
def exist_by_did(did,user):
	if not user.has_key('devices'): return False
	for device in user['devices']:
		if device.has_key['did'] and device['did'] == did:
			return True
	return False

#添加设备
def add(phone,owner,user):
	device = {
		'phone':phone,
		'active_code':StringUtil.active_code_generator(),
		'active':False,
		'owner':owner,
		'time':time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
	}
	user['devices'].append(device)
	UserCollection.update({'tid':user['tid']},user)
	return RESPONSE.SUCCESS

#展示设备列表
def list(user):
	for device in user['devices']:
		device['tid'] = user['tid']
	return user['devices']

#返回设备详细信息
def detail(did,user):
	for device in user['devices']:
		if device['did'] == did:
			cid = device['cid'] if device.has_key('cid') else "N/A"
			imei = device['imei'] if device.has_key('imei') else "N/A"
			return {
				'loc_interval':user['loc_interval'],
				'loc_mode':user['loc_mode'],
				'did':did,
				'cid':cid,
				'imei':imei
			}
	return {}




