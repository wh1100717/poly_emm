#!/usr/bin/env python
# -*- coding: utf-8 -*-

from util import MongoUtil

BlackListCollection = MongoUtil.db.blacklist
UserCollection = MongoUtil.db.user
#获取黑名单list
def list(token,did,user):
	if not UserCollection.find_one({'token':token}): return {'status':0, 'desc':'wrong token'}
	blacklist = BlackListCollection.find_one({'did':did})
	return {'status':1, 'apps':blacklist['apps']} if blacklist else {'status':0, 'desc':'no blacklist'}
		
#添加app到黑名单
def app_insert(user,did,apps):
	blacklist = BlackListCollection.find_one({'did':did})
	if blacklist:
		blacklist['apps'] += apps
	else:
		blacklist = {
			'did':did,
			'apps':[apps]
		}
	BlackListCollection.save({'did':did},blacklist)
	return 'success'
#删除app到黑名单
def delete(user,did,appid_list):
	blacklist = BlackListCollection.find_one({'did':did})
	if not blacklist: return {'wrong did'}
	apps = blacklist['apps']
	for i in range(len(apps)):
		app = apps[i]
		if app['appId'] in appid_list:
			del(apps[i])
	BlackListCollection.update({'did':did},blacklist)
	return 'success'
