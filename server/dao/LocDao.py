#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dao import UserDao

UserCollection = MongoUtil.db.user

def update(token,uid,did,loc_info):
	user = UserDao.get_user_by_token(token)
	if not user: return {'status':0, 'desc':'wrong token'}
	device_list = user['device']
	for device in device_list:
		if device['did'] == did and device['uid'] == uid:
			device['loc_info'] = loc_info
			UserCollection.update({'email':user['email']},user)
			return {'status':1}
	return {'status':0, 'desc':'wrong did or uid'}
