#!/usr/bin/env python
# -*- coding: utf-8 -*-

from util import MongoUtil
from dao import UserDao
from dao import DeviceDao
from status import *
import time

PolicyCollection = MongoUtil.db.policy

def add(policy_name,platform,user):
	policy = {
		'policy_name':policy_name,
		'policy_id':MongoUtil.getNextSequence('policy_id'),
		'platform':platform,
		'tid': user['tid'],
		'time':time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),
		'content':''
	}
	PolicyCollection.insert(policy)
	return RESPONSE.SUCCESS

def delete(policy_id,user):
	PolicyCollection.remove({'policy_id':policy_id})
	return RESPONSE.SUCCESS

def edit(policy_id,policy_content,user):
	policy = PolicyCollection.find({'policy_id':policy_id})
	policy['policy_content'] = policy_content
	policy_content.update({'policy_id':policy_id},policy)
	return RESPONSE.SUCCESS

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