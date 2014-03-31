#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib
from util import MongoUtil
from util import StringUtil

UserCollection = MongoUtil.db.user

def get_user_by_email(email):
	return UserCollection.find_one({'email':email})

def get_user_by_phone(phone):
	return UserCollection.find_one({'phone':phone})

def get_user_by_tid(tid):
	return UserCollection.find_one({'tid':int(tid)})

def get_user_by_token(token):
	return UserCollection.find_one({'token':token})

def register(email_or_phone,enroll_type,user_name,pwd):
	user = {
		'tid': MongoUtil.getNextSequence('tid'),
		'user_name': user_name,
		'pwd': hashlib.md5(pwd).hexdigest(),
		'role': 'admin',
		'active': True,
		'token': StringUtil.token_generator(),
		'loc_interval': 0,
		'loc_mode': 0,
		'devices':[]
	}
	if enroll_type == 'email':
		user['email'] = email_or_phone
	else:
		user['phone'] = email_or_phone
	UserCollection.insert(user)
