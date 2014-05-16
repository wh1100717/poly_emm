#!/usr/bin/env python
# -*- coding: utf-8 -*-
from util import MongoUtil
from dao import UserDao
from dao import DeviceDao
from status import *
UserCollection = MongoUtil.db.user
def save_info(push_type,push_type_id,device_lists,user):
	cids=[]
	print push_type
	print push_type_id
	print device_lists
	dev_list=[]
	for i in device_lists:
		dev_list.append(str(i))
	print dev_list
	for i in range(len(DeviceDao.get_devices_by_user(user))):
		if user['devices'][i].has_key('did') and user['devices'][i]['did'] in dev_list:
			print user['devices'][i]
			print user['devices'][i]['cid']
			user['devices'][i]['pull_info'].append({'type':push_type,'push_type_id':push_type_id})
			UserCollection.update({'tid':user['tid']},user)
			cids.append(user['devices'][i]['cid'])
	return cids
def list(user):
	active_list=[]
	for device in DeviceDao.get_devices_by_user(user):
	# device['tid'] = user['tid']
		if device['active'] == True:
			active_list.append(device)
	return active_list