#!/usr/bin/env python
# -*- coding: utf-8 -*-
from dao import UserDao
from dao import DeviceDao
from status import *
from util import MongoUtil

UserCollection = MongoUtil.db.user

def enroll(tid, active_code, phone):
	user = UserDao.get_user_by_tid(tid)
	if not user: return RESPONSE.WRONG_TID
	devices = DeviceDao.get_devices_by_user(user)
	for device in devices:
		if device['phone'] == phone:
			if device['active_code'] == active_code:
				if device['active'] == True: 
					return RESPONSE.ALREADY_ACTIVED
				device['active'] = True
				UserCollection.update({'tid':user['tid']},user)
				RESPONSE.ENROLL_SUCCESS['token'] = user['token']
				print RESPONSE.ENROLL_SUCCESS['token'] 
				return RESPONSE.ENROLL_SUCCESS
			else:
				return RESPONSE.WRONG_ACTIVE_CODE
	return RESPONSE.WRONG_PHONE

def initial(token,phone,did,cid,imei):
	user = UserDao.get_user_by_token(token)
	if not user: return RESPONSE.WRONG_TOKEN
	devices = DeviceDao.get_devices_by_user(user)
	for device in devices:
		if device['phone'] == phone:
			device['did'] = did
			device['cid'] = cid
			device['imei'] = imei
			UserCollection.update({'tid':user['tid']},user)
			#TODO 需要增加client对初始化配置信息
			RESPONSE.INITIAL_SUCCESS['initial'] = {}
			return RESPONSE.INITIAL_SUCCESS
	return RESPONSE.WRONG_PHONE

def pull(token, did):
	user = UserDao.get_user_by_token(token)
	if not user: return RESPONSE.WRONG_TOKEN
	devices = DeviceDao.get_devices_by_user(user)
	for device in devices:
		if device['did'] == did:

			#TODO 需要将具体的信息返回回去
			RESPONSE.PULL_SUCCESS['data'] = device['pull_info']
			device['pull_info']=[]
			UserCollection.update({'token':user['token']},user)
			return RESPONSE.PULL_SUCCESS
	return RESPONSE.WRONG_DID

def resp(token, did):
	user = UserDao.get_user_by_token(token)
	if not user: return RESPONSE.WRONG_TOKEN
	devices = DeviceDao.get_devices_by_user(user)
	for device in devices:
		if device['did'] == did:
			#TODO 需要进行一些数据清理工作
			return RESPONSE.SUCCESS
	return RESPONSE.WRONG_DID

