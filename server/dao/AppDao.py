#!/usr/bin/env python
# -*- coding: utf-8 -*-

from util import MongoUtil
from dao import UserDao

AppCollection = MongoUtil.db.app

def update(token,did,apps):
	user = UserDao.get_user_by_token(token)
	if not user: return {'status':0, 'desc':'wrong token'}

	device_app = AppCollection.find_one({'did':'did'})
	print "apps: ",apps
	print "device_app: ",device_app
	if device_app:
		device_app['apps'] = apps
	else:
		device_app = {
			'did':did,
			'apps':apps
		}
	print "device_app: ", device_app
	AppCollection.update({'did':did}, device_app, upsert=True)
	return {'status':1}

def list(did, user):
	device_list = user['device']
	for device in device_list:
		if device['did'] == did:
			device_app = AppCollection.find_one({'did':did})
			return device_app['apps']
	return []
