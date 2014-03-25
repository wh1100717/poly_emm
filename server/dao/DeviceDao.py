#!/usr/bin/env python
# -*- coding: utf-8 -*-
from util import MongoUtil
from util import StringUtil
from dao import UserDao
import time

UserCollection = MongoUtil.db.user

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
	UserCollection.update({'email':user['email']},user)
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
	for device in user['device']:
		device['tanent_id'] = user['tanent_id']
	return user['device']

#获取激活设备列表
def active_list(user,page_size,page_start):
	if not user.has_key('device'): return []
	page_index = 0
	result = []
	for device in user['device']:
		print 'page_index', page_index
		print 'page_size', page_size
		if page_index < page_start:
			page_index += 1
			continue
		if page_size <= 0:
			break
		if device['active'] == True:
			device['tanent_id'] = user['tanent_id']
			result.append(device)
			page_size -= 1
	print result
	return result

def enroll(uid, active_code, tanent_id):
	user = UserDao.get_user_by_tanent_id(tanent_id)
	if not user: return {'status':0,'desc':'wrong tanent_id'}
	device_list = user['device']
	for device in device_list:
		if device['uid'] == uid:
			if device['active_code'] == active_code:
				if device['active'] == True: return {'status':0, 'desc':'already actived'}
				device['active'] = True
				UserCollection.update({'email':user['email']},user)
				return {'status':1, 'token':user['token']}
			else:
				return {'status':0, 'desc':'wrong active code'}
	return {'status':0, 'desc':'wrong uid'}

def update(token,uid,did,cid,imei):
	user = UserDao.get_user_by_token(token)
	if not user: return {'status':0,'desc':'wrong token'}
	device_list = user['device']
	for device in device_list:
		if device['uid'] == uid:
			device['did'] = did
			device['imei'] = imei
			device['cid'] = cid
			UserCollection.update({'email':user['email']},user)
			return {'status':1}
	return {'status':0,'desc':'wrong uid'}

def config(token,did):
	user = UserDao.get_user_by_token(token)
	if not user: return {'status':0, 'desc':'wrong token'}
	device_list = user['device']
	for device in device_list:
		if device['did'] == did:
			return {'status':1, 'loc_interval':user['loc_interval'], 'loc_mode':user['loc_mode']}
	return {'status':0, 'desc':'wrong did'}








