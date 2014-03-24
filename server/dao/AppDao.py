#!/usr/bin/env python
# -*- coding: utf-8 -*-

from util import MongoUtil
from dao import UserDao

AppCollection = MongoUtil.db.app

def update(token,did,apps):
	user = UserDao.get_user_by_token(token)
	if not user: return {'status':0, 'desc':'wrong token'}

	device_app = AppCollection.find_one({'did':'did'})
	if device_app:
		device_app['apps'] = apps
	else:
		device_app = {
			'did':did,
			'apps':apps
		}
	AppCollection.save({'did':did}, device_app)
	return {'status':1}