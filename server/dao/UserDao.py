#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib
from util import MongoUtil

UserCollection = MongoUtil.db.user

def get_user(username):
	user_store = [{'username':'eric', 'password':hashlib.md5('123').hexdigest()}]
	for user in user_store:
		print username
		if user['username'] == username:
			return user
	return None

def register(email,username,pwd):
	user = {
		'_id': MongoUtil.getNextSequence('uid'),
		'email': email,
		'username': username,
		'pwd': hashlib.md5(pwd).hexdigest()
	}
	UserCollection.insert(user)
	return 'success'