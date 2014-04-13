#!/usr/bin/env python
# -*- coding: utf-8 -*-

from util import MongoUtil
from dao import UserDao
from dao import DeviceDao
from status import *

UserCollection = MongoUtil.db.user

def update(token,did,apps):
	user = UserDao.get_user_by_token(token)
	if not user: return {'status':0, 'desc':'wrong token'}

	devices = DeviceDao.get_devices_by_user(user)
	devices['apps'] = apps
	UserCollection.update({'tid':user['tid']},user)
	return RESPONSE.SUCCESS

def list(did, user):
	device_list = DeviceDao.get_devices_by_user(user)
	for device in device_list:
		if device.has_key('did') and device['did']== did:
			if device.has_key('apps'):
				return device['apps']
			else:
				return []
	return []
