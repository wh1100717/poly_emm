#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib
from util import MongoUtil
from util import StringUtil

UserCollection = MongoUtil.db.user

def get_user(user_name):
	return UserCollection.find_one({'user_name':user_name})

def get_user_by_user_id(user_id):
	return UserCollection.find_one({'user_id':user_id})

def get_user_by_tanent_id(tanent_id):
	return UserCollection.find_one({'tanent_id':tanent_id})

def get_user_by_token(token):
	return UserCollection.find_one({'token':token})

def register(email,user_name,pwd):
	user = {
		'tanent_id': MongoUtil.getNextSequence('tanent_id'),
		'user_id': email,
		'user_name': user_name,
		'pwd': hashlib.md5(pwd).hexdigest(),
		'role': 'admin',
		'active': True,
		'token': StringUtil.token_generator()
	}
	UserCollection.insert(user)
	return 'success'
