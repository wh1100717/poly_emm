#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib

def get_user(username):
	user_store = [{'username':'eric', 'password':hashlib.md5('123').hexdigest()}]
	for user in user_store:
		print username
		if user['username'] == username:
			return user
	return None

def register(email,username,password):
	return 'success'