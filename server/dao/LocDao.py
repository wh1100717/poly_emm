#!/usr/bin/env python
# -*- coding: utf-8 -*-

from util import MongoUtil
from dao import UserDao

LocCollection = MongoUtil.db.loc

def update(token,did,loc_info):
	user = UserDao.get_user_by_token(token)
	if not user: return {'status':0, 'desc':'wrong token'}
	device_loc = LocCollection.find_one({'did':did})
	if device_loc:
		device_loc['loc_info'].append(loc_info)
	else:
		device_loc = {
			'did':did,
			'loc_info': [loc_info]
		}
	LocCollection.update({'did':did}, device_loc, upsert=True)
	return {'status':1}
