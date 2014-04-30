#!/usr/bin/env python
# -*- coding: utf-8 -*-

from util import MongoUtil
from dao import UserDao
from dao import DeviceDao
from status import *
import time

PolicyCollection = MongoUtil.db.policy
UserCollection = MongoUtil.db.user

def add(policy_id,policy_name,policy_content,platform,user):
	policy = {
		'policy_name':policy_name,
		
		'platform':platform,
		'tid': user['tid'],
		'time':time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),
		'content':policy_content
		}
	if policy_id == "0":
		policy['policy_id'] = MongoUtil.getNextSequence('policy_id')
		PolicyCollection.insert(policy)
	else:	
		
 		PolicyCollection.update({'policy_id':int(policy_id)},{"$set":policy})
	
	return RESPONSE.SUCCESS

def delete(policy_id,user):
	PolicyCollection.remove({'policy_id':int(policy_id)})
	return RESPONSE.SUCCESS

def edit(policy_id,user):
	policy = PolicyCollection.find({'policy_id':int(policy_id)})
	
	response = RESPONSE.LIST_SUCCESS
	
	data = {}
	data['policy_name']=policy[0]['policy_name']
	data['policy_id']=policy[0]['policy_id']
	data['platform']=policy[0]['platform']
	data['content']=policy[0]['content']
	response['data'] = data
	print response
	return response


# def edit(policy_id,policy_name,policy_content,user):
# 	policy = PolicyCollection.find({'policy_id':policy_id})
# 	policy['policy_content'] = policy_content
# 	policy['policy_name'] = policy_name
# 	# policy_content.update({'policy_id':policy_id},policy)
# 	PolicyCollection.update(policy)
# 	return RESPONSE.SUCCESS

def list(user):
	tid = user['tid']
	policy_lists = PolicyCollection.find({'tid':tid})
	data = []
	for policy_list in policy_lists:
		policy_info = {}
		policy_info['policy_id'] = policy_list['policy_id']
		policy_info['policy_name'] = policy_list['policy_name']
		policy_info['platform'] = policy_list['platform']
		policy_info['time'] = policy_list['time']
		data.append(policy_info)
	return data

def detail(policy_id):
	# policy_list = PolicyCollection.find({'policy_id':policy_id})
	# data = []
	# for policy_list in policy_lists:
	# 	policy_info = {}
	# 	policy_info['policy_name'] = policy_list['policy_name']
	# 	policy_info['platform'] = policy_list['platform']
	# 	policy_info['content'] = policy_list['content']
	# 	data.append(policy_info)
	# 	print data
	tid = user['tid']
	policy_lists = PolicyCollection.find({'tid':tid})
	data = []
	for policy_list in policy_lists:
		policy_info = {}
		policy_info['policy_name'] = policy_list['policy_name']
		policy_info['platform'] = policy_list['platform']
		policy_info['content'] = policy_list['content']
		data.append(policy_info)
		print data
	return data

def push(policy_id,device_lists,user):
	time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
	policy = PolicyCollection.find('policy_id',policy_id)
	policy['policy_history'] = [{'time':time,'device_lists':device_lists}]
	PolicyCollection.update({'policy_id':policy_id},policy)
	cids = []
	for device in user['devices']:
		if device['did'] in device_lists:
			device['pull_info'] = {'type':'policy','policy_id':policy_id}
			cids.append(device['cid'])
	UserCollection.update({'tid':user['tid']},user)
	return cids