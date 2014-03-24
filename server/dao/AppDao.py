#!/usr/bin/env python
# -*- coding: utf-8 -*-

from util import MongoUtil
from dao import UserDao

UserCollection = MongoUtil.db.user

def update(token,uid,did,app_list):
	user = UserDao.get_user_by_token(token)
	if not user: return {'status':0, 'desc':'wrong token'}
	device_list = user['device']
	for device in device_list:
		if device['did'] == did and device['uid'] == uid:
			#TODO 需要处理具体app_list的存入操作，目前不是很确定app_list是否存放在user.device下
			UserCollection.update({'email':user['email']},user)
			return {'status':1}
	return {'status':0, 'desc':'wrong did or uid'}
