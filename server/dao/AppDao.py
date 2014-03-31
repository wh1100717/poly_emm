#!/usr/bin/env python
# -*- coding: utf-8 -*-

from util import MongoUtil
from dao import UserDao
from status import *

UserCollection = MongoUtil.db.user

def update(token,did,apps):
	user = UserDao.get_user_by_token(token)
	if not user: return {'status':0, 'desc':'wrong token'}

	devices = user['devices']
	devices['apps'] = apps
	UserCollection.update({'tid':user['tid']},user)
	return RESPONSE.SUCCESS

def list(did, user):
	device_list = user['device']
	for device in device_list:
		if device.has_key('did') and device['did']== did:
			if device.has_key('apps'):
				return device['apps']
			else:
				return []
	return []
