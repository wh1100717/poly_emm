#!/usr/bin/env python
# -*- coding: utf-8 -*-

#=======================
#### file: testAppDao.py ####
#=======================

import sys
import os
import nose
from nose import with_setup


c_path = os.getcwd()
base_path = c_path[:c_path.rfind("backend_tests")]
sys.path.append(base_path)

##所有的测试模块import在这下面：

from dao import UserDao
from util import StringUtil
from dao import DeviceDao
from dao import BlackListDao
from dao import AppDao
from dao import LocDao

##################初始化######################
# g = {}

# def setup_module(module):
# 	print "单元测试开始"
# 	g = {
# 		'email':123
# 	}

# def test_abc():
# 	print g['a']
# 	assert g['a']==1

##################UserDao##########################

email = StringUtil.token_generator() + "@qq.com"
user_name = 'xiaolin'
pwd = 'zxldmv'
enroll_type='email'
'''
用户注册流程
'''
def test_register():
	result = UserDao.register(email, enroll_type,user_name, pwd)
	assert result == 'success'

def test_get_user_by_email():
	user = UserDao.get_user_by_email(email)
	assert user['email'] == email

def test_get_user_by_tid():
	user = UserDao.get_user_by_email(email)
	user2 = UserDao.get_user_by_tid(user['tid'])
	assert user2['email'] == email

def test_get_user_by_token():
	user = UserDao.get_user_by_email(email)
	user2 = UserDao.get_user_by_token(user['token'])
	assert user2['email'] == email


##################UserDao Done##########################



##################DeviceDao##########################

uid = StringUtil.active_code_generator()
owner = 'zxl'
did = '1234'
cid = '12345'
imei = '123456'

def test_add():
	user = UserDao.get_user_by_email(email)
	result = DeviceDao.add(uid,owner,user)
	assert result == 'success'

def test_exist():
	user = UserDao.get_user_by_email(email)
	device = DeviceDao.exist(uid,owner,user)
	assert device == True

def test_register_list():
	user = UserDao.get_user_by_email(email)
	list1 = DeviceDao.register_list(user)
	assert list1 != []

def test_enroll():
	user = UserDao.get_user_by_email(email)
	device = user['device']
	active_code = ""
	for d in device:
		if d['uid'] == uid:
			active_code = d['active_code']
	tid = user['tid']

	result = DeviceDao.enroll(uid,active_code,tid)
	assert result['status'] == 1

def test_update_device():
	user = UserDao.get_user_by_email(email)
	result = DeviceDao.update(user['token'],uid,did,cid,imei)
	assert result['status'] == 1

def test_config():
	user = UserDao.get_user_by_email(email)
	result = DeviceDao.config(user['token'],did)
	assert result['status'] == 1
	

##################DeviceDao Done##########################



##################BlackListDao##########################

did = '1234'
app_id = StringUtil.active_code_generator()
apps = [{'appName':"asd",'appId':app_id,'version':2.1}]
appId_list = [str(app_id)]


def test_insert():
	user = UserDao.get_user_by_email(email)
	result = BlackListDao.app_insert(user,did,apps)
	assert result == 'success'

def test_list():
	user = UserDao.get_user_by_email(email)
	result = BlackListDao.list(user['token'],did,user)
	assert result['status'] == 1

def test_delete():
	user = UserDao.get_user_by_email(email)
	result = BlackListDao.delete(user,did,appId_list)
	assert result == 'success'



##################BlackListDao Done##########################


##################AppDao##########################

did = '1234'
app_id = StringUtil.active_code_generator()
apps = [
	{'appName':"asd1",'appId':app_id,'version':'2.1'},
	{'appName':"asd2",'appId':app_id,'version':'2.2'}
]

def test_update_app():
	user = UserDao.get_user_by_email(email)
	result = AppDao.update(user['token'],did,apps)
	assert result['status'] == 1
	

##################AppDao Done##########################


##################LocDao##########################

loc_info = [
			{'timestamp':StringUtil.active_code_generator(),
				'mode':StringUtil.active_code_generator(),
				'interval':StringUtil.active_code_generator(),
				'lat':StringUtil.active_code_generator(),
				'long':StringUtil.active_code_generator()}
			]
did = '1234'
def test_update_loc():
	user = UserDao.get_user_by_email(email)
	result = LocDao.update(user['token'],did,loc_info)
	assert result['status'] == 1

##################LocDao Done##########################


##################MsgDao##########################



##################MsgDao Done##########################



# # from dao import AppDao



# def teardown_module(module):
# 	print "单元测试结束"

# def setup_func():
# 	print "set up test fixtures"

# def teardown_func():
# 	print "tear down test fixtures"

# def test_should_be_implemented():
# 	print "\n1. 	ShouldBeImpelemented测试开始"
# 	the_target_result = "Specific result should be outputed using below method"
# 	assert True

# def test_demo():
# 	print "\n2. 	TestDemo测试开始"
# 	the_target_result = "hello world"


# def test_divid_function():
# 	print "\n3. 	add()测试开始"
# 	assert divid(2, 1) == 2
# 	assert divid(4, 2) == 2
# 	assert divid(20, 10) == 2
# 	assert divid(20, 0) == 0



# def divid(a,b):
# 	if b == 0:
# 		return 0
# 	else:
# 		return a/b


if __name__ == "__main__":
	test_get_app_count()