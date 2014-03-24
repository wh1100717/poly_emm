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
	devices = user['device']
	device_register_lists=[]
	for device in devices:
		device_register_list={
			'tanent_id':user['tanent_id'],
			'uid':device['uid'],
			'owner':device['owner'],
			'active_code':device['active_code'],
			'active':device['active'],
			'time':device['time']
		}
		device_register_lists.append(device_register_list)
	return device_register_lists

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

def config(token,uid,did):
	user = UserDao.get_user_by_token(token)
	if not user: return {'status':0, 'desc':'wrong token'}
	return {'status':1, 'loc_interval':user['loc_interval'], 'loc_mode':user['loc_mode']}







